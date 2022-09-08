from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import uuid
import datetime
import itertools
import os

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secrtekeyfornow'
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')
# Add the database 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'

# folder for images 
UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
    company = db.Column(db.String(200), nullable=False)
    referenceNo = db.Column(db.String(200))
    description = db.Column(db.Text(), nullable=False)
    salary = db.Column(db.Float)
    location = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    parttime = db.Column(db.Boolean, default=False, nullable=False)
    fourday = db.Column(db.Boolean, default=False, nullable=False)
    childcare = db.Column(db.Boolean, default=False, nullable=False)

"""
class UsersShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

class JobsShema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("title", "datetime", "created_by","datetime","description","salary","data")
"""
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
        print(request.form.get('psw'), request.form.get('psw-repeat'))
        if(request.form.get('psw') != request.form.get('psw-repeat')):
            flash('Passwords did not match') 
            return redirect(url_for('register'))
        elif(checkEmail):
            flash('Email already exits') 
            return redirect(url_for('register'))
        else: 
            hashed_password = generate_password_hash(request.form.get('psw'))
            user = Users(name = request.form.get('compnay'), email = request.form.get('email'), userType= userType, password_hash = hashed_password)
            db.session.add(user)
            db.session.commit()
            flash('User registered. Plase login')
            return render_template('login.html') 

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        print(request.form)
        user = Users.query.filter_by(email = request.form.get('email')).first()
        if(user):
            if(check_password_hash(user.password_hash, request.form.get('psw'))):
                #login user
                login_user(user)
                flash('Hi '+ user.name + '! Thanks for trying to make a world more equal place')
                return redirect(url_for('jobposts'))
            else:
                flash('Wrong email or password')
                return redirect(url_for('login'))
        else:
            flash('Wrong email or password')
            return redirect(url_for('login'))

@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/jobposts', methods = ['GET'])
def jobposts():
    jobs = Jobs.query.order_by(Jobs.datetime.desc()).all()
    for job in jobs:
        user = Users.query.filter_by(id = job.created_by).first()
        job.username = user.name
    if request.method == 'GET':
        return render_template('jobposts.html', jobs=jobs)

@app.route('/badgeview/<int:id>', methods = ['GET'])
def badgeview(id):

    jobs = Jobs.query.order_by(Jobs.datetime.desc()).all()
    for job in jobs:
        user = Users.query.filter_by(id = job.created_by).first()
        job.username = user.name

    if id == 1:
        jobs = Jobs.query.filter(Jobs.childcare.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Childcare")
    if id == 2:
        jobs = Jobs.query.filter(Jobs.parttime.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Part time work")
    if id == 3:
        jobs = Jobs.query.filter(Jobs.fourday.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Four day week")
    if request.method == 'GET':
        return render_template('badgeview.html', jobs=jobs)

@app.route('/jobposts/delete/<int:id>', methods = ['POST'])
def jobposts_delete(id):
    post_to_delte = Jobs.query.get(id)
    try:
        db.session.delete(post_to_delte)
        db.session.commit()
        # message that confirms deletion 
        return render_template('jobposts.html')
    except:
        print('error handler')

@app.route('/profile', methods = ['GET', 'POST'])
@login_required
def profile():
    if request.method == 'GET':
        return render_template('profile.html', user = current_user)

    if request.method == 'POST':
        user = Users.query.filter_by(id = current_user.id).first()
        message = ''

        if(request.form.get('psw') and request.form.get('psw-repeat')):
            if(request.form.get('psw') == request.form.get('psw-repeat')):   
                hashed_password = generate_password_hash(request.form.get('psw'))
                user.password_hash = hashed_password
                db.session.commit()
                message += ' Password Updated.'
       
        if(request.form.get('name')):
            if(request.form.get('name') != user.name):
                user.name = request.form.get('name')
                db.session.commit()
                message += ' Name Updated.'
        
        checkEmail = Users.query.filter_by(email = request.form.get('email')).first()
        if(request.form.get('email')):
            if(checkEmail):
                # emial exists
                if(request.form.get('email') != user.email):
                    message += ' Email NOT Updated. The email you choose is already taken.'
            else:
                user.email = request.form.get('email')
                db.session.commit()
                message += ' Email Updated.'
        
        if(message == ''):
            message = 'No changes were made.'
        flash(message)
        return render_template('profile.html', user = current_user)

@app.route('/search')
def search():
    queryterm = request.args.get('q')
    # jobs = Jobs.query.order_by(Jobs.datetime.desc()).all()
    jobs = Jobs.query.filter(Jobs.title.like('%' + queryterm + '%') | Jobs.description.like('%' + queryterm + '%') | Jobs.company.like('%' + queryterm + '%') | Jobs.location.like('%' + queryterm + '%'))
    return render_template('searchresults.html', jobs=jobs, searchterm=queryterm)

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

        referenceNo = ''
        if(request.form.get('refnum')):
            referenceNo = request.form.get('refnum')



        job = Jobs( title = request.form.get('title'), 
                    referenceNo = referenceNo, 
                    description = request.form.get('discription'), 
                    location = request.form.get('location'), 
                    company = request.form.get('company'), 
                    salary = salary, 
                    created_by = current_user.id, 
                    parttime=parttime, 
                    fourday=fourday, 
                    childcare=childcare
        )

        db.session.add(job)
        db.session.commit()
        flash('Your job was posted.')
        return redirect(url_for('jobposts'))


# API 
"""
@app.route('/api-jobs/all', methods = ['GET'])
def api_partall():
    if request.method == 'GET':   
        jobs = Jobs.query.all()
        for job in jobs:
            user = Users.query.filter_by(id = job.created_by).first()
            job.data = user.name
    
        job_schema = JobsShema()
        output = job_schema.dump(jobs, many=True)
        return jsonify({'jobs': output})
"""

@app.route('/jobposts/parttime', methods = ['GET'])
def api_parttime():
    if request.method == 'GET':   
        return findCorrectJobs('parttime')

@app.route('/jobposts/fourday', methods = ['GET'])
def api_fourday():
    if request.method == 'GET':   
        return findCorrectJobs('fourday')

@app.route('/jobposts/childcare', methods = ['GET'])
def api_childcare():
    if request.method == 'GET': 
        return findCorrectJobs('childcare')

def findCorrectJobs(typeofbadge):
    kwargs = {typeofbadge : True}
    jobs = Jobs.query.filter_by(**kwargs)
    for job in jobs:
        user = Users.query.filter_by(id = job.created_by).first()
        job.username = user.name
    return render_template('jobposts.html', jobs=jobs)

