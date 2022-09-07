from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import itertools



app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secrtekeyfornow'


# Add the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

# Initialize the database 
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Flaks Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

# Create Model
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password_hash = db.Column(db.String(150), nullable=False)
    userType = db.Column(db.String(100), nullable=False)
    
    @property
    def password(self):
        raise AttributeError('Password not readable.')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_pass(self, password):
        return check_password_hash(self.password_hash, password)

class Jobs(db.Model):
    job_id = db.Column(db.Integer, primary_key = True)    
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    salary = db.Column(db.Float)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    parttime = db.Column(db.Boolean, default=False, nullable=False)
    fourday = db.Column(db.Boolean, default=False, nullable=False)
    childcare = db.Column(db.Boolean, default=False, nullable=False)

class UsersShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

class JobsShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("title", "datetime", "created_by","datetime","description","salary","data")

@app.route('/', methods = ['GET'])
def index():
    return render_template('home.html')


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    if request.method == 'POST':
        checkEmail = Users.query.filter_by(email = request.form.get('email')).first()
        userType = ''
        if(request.form.get('userType')):
            userType = 'employer'
        else:
            userType = 'employee'

        if(request.form.get('psw') != request.form.get('psw-repeat')):
            return 'Message that passwords need to match'
        elif(checkEmail):
            return 'Message that emial exists'
        else: 
            hashed_password = generate_password_hash(request.form.get('psw'))
            user = Users(name = request.form.get('compnay'), email = request.form.get('email'), userType= userType, password_hash = hashed_password)
            db.session.add(user)
            db.session.commit()
            return render_template('login.html') 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        user = Users.query.filter_by(email = request.form.get('email')).first()
        if(user):
            if(check_password_hash(user.password_hash, request.form.get('psw'))):
                #login user
                login_user(user)
                return render_template('jobposts.html')
            else:
                return render_template('login.html')
        else:
            return render_template('login.html')


@app.route('/jobposts', methods = ['GET'])
def jobposts():
    jobs = Jobs.query.all()
    created_by = []
    for job in jobs:
        user = Users.query.filter_by(id = job.created_by).first()
        created_by.append(user.name)
    if request.method == 'GET':
        return render_template('jobposts.html', packed=zip(jobs, created_by))

# work in progess
#@app.route('/jobposts/delete/<int:id>', methods = ['POST'])
#def jobposts_delete(id):
#    post_to_delte = Jobs.query

@app.route('/addjob', methods = ['GET','POST'])
@login_required
def addjob():
    if request.method == 'GET':   
        return render_template('addjob.html')

    if request.method == 'POST':

        childcare = "childcare" in request.form
        parttime = "parttime" in request.form
        fourday = "fourday" in request.form
        salary = 0.0
        if(request.form.get('salary')):
            salary = request.form.get('salary')
        job = Jobs(title = request.form.get('title'), description = request.form.get('description'), salary = salary, created_by = current_user.id, parttime=parttime, fourday=fourday, childcare=childcare)
        db.session.add(job)
        db.session.commit()
        return render_template('jobposts.html')


# API 
@app.route('/api-jobs/parttime', methods = ['GET'])
def api_parttime():
    if request.method == 'GET':   
        return findCorrectJobs('parttime')

@app.route('/api-jobs/fourday', methods = ['GET'])
def api_fourday():
    if request.method == 'GET':   
        return findCorrectJobs('fourday')

@app.route('/api-jobs/childcare', methods = ['GET'])
def api_childcare():
    if request.method == 'GET': 
        return findCorrectJobs('childcare')

def findCorrectJobs(typeofbadge):
    print(typeofbadge)
    kwargs = {typeofbadge : True}
    jobs = Jobs.query.filter_by(**kwargs)
    for job in jobs:
        user = Users.query.filter_by(id = job.created_by).first()
        job.data = user.name
        print(job.data)
    job_schema = JobsShema()
    output = job_schema.dump(jobs, many=True)
    return jsonify({'jobs': output})