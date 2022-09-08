from flask import Flask, jsonify, request, render_template, flash, redirect, url_for, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow, fields
from flask_cors import CORS
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
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
    # badge booleans
    lgbt = db.Column(db.Boolean, default=False, nullable=False)
    genderbalance = db.Column(db.Boolean, default=False, nullable=False)
    insurance = db.Column(db.Boolean, default=False, nullable=False)
    mentoring = db.Column(db.Boolean, default=False, nullable=False)
    zero_harrassment = db.Column(db.Boolean, default=False, nullable=False)
    no_pay_gap = db.Column(db.Boolean, default=False, nullable=False)
    diverse_interview = db.Column(db.Boolean, default=False, nullable=False)
    open_to_bootcamp = db.Column(db.Boolean, default=False, nullable=False)
    open_to_career_gap = db.Column(db.Boolean, default=False, nullable=False)
    parttime = db.Column(db.Boolean, default=False, nullable=False)
    fourday = db.Column(db.Boolean, default=False, nullable=False)
    childcare = db.Column(db.Boolean, default=False, nullable=False)
    remote_work = db.Column(db.Boolean, default=False, nullable=False)
    experience_requirements = db.Column(db.Boolean, default=False, nullable=False)
    flexible_hours = db.Column(db.Boolean, default=False, nullable=False)

class Savedjobs(db.Model):
    savedjobs_id = db.Column(db.Integer, primary_key = True)   
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id')) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
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
            flash('User registered.')
            login_user(user)
            return redirect(url_for('index'))

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
                return redirect(url_for('index'))
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
    if request.method == 'GET':
        jobs = Jobs.query.order_by(Jobs.datetime.desc()).all()
        for job in jobs:
            user = Users.query.filter_by(id = job.created_by).first()
            job.username = user.name
            if(current_user.is_authenticated):
                savedjobs = Savedjobs.query.filter_by(job_id = job.job_id, user_id = current_user.id).first()
                if(savedjobs):
                    job.saved = 'Remove'
                else:
                    job.saved = 'Save Job'


        return render_template('jobposts.html', jobs=jobs)

@app.route('/badgeview/<int:id>', methods = ['GET'])
def badgeview(id):

    jobs = Jobs.query.order_by(Jobs.datetime.desc()).all()
    for job in jobs:
        user = Users.query.filter_by(id = job.created_by).first()
        job.username = user.name

    if id == 1:
        jobs = Jobs.query.filter(Jobs.lgbt.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="LGBTQIA+ Friendly")
    if id == 2:
        jobs = Jobs.query.filter(Jobs.genderbalance.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Good gender balance in workplace")
    if id == 3:
        jobs = Jobs.query.filter(Jobs.insurance.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Family Health Insurance")
    if id == 4:
        jobs = Jobs.query.filter(Jobs.mentoring.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Mentor System")
    if id == 5:
        jobs = Jobs.query.filter(Jobs.zero_harrassment.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Zero-tolerance harrassment policy")
    if id == 6:
        jobs = Jobs.query.filter(Jobs.no_pay_gap.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="No pay gap")
    if id == 7:
        jobs = Jobs.query.filter(Jobs.diverse_interview.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Diverse Interview Panel")
    if id == 8:
        jobs = Jobs.query.filter(Jobs.open_to_bootcamp.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Open to bootcamp/conversion graduates")
    if id == 9:
        jobs = Jobs.query.filter(Jobs.open_to_career_gap.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Open to applicants with a career gap")
    if id == 10:
        jobs = Jobs.query.filter(Jobs.parttime.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Part-time schedule available")
    if id == 11:
        jobs = Jobs.query.filter(Jobs.childcare.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Childcare")
    if id == 12:
        jobs = Jobs.query.filter(Jobs.remote_work.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Remote work option")
    if id == 13:
        jobs = Jobs.query.filter(Jobs.childcare.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Childcare")
    if id == 14:
        jobs = Jobs.query.filter(Jobs.experience_requirements.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Realistic experience requirements")
    if id == 15:
        jobs = Jobs.query.filter(Jobs.flexible_hours.is_(True)).order_by(Jobs.datetime.desc())
        return render_template('badgeview.html', jobs=jobs, pagename="Flexible hours")

    
    if request.method == 'GET':
        return render_template('badgeview.html', jobs=jobs)

@app.route('/jobposts/delete/<int:id>', methods = ['POST'])
@login_required
def jobposts_delete(id):
    post_to_delete = Jobs.query.get(id)
    user = Users.query.filter_by(id = post_to_delete.created_by).first()
    if(user.id == current_user.id):
        db.session.delete(post_to_delete)
        db.session.commit()
        flash('Job post has been deleted.')
        return render_template('jobposts.html')
    else:
        flash('Ooops! Something went wrong.')
        return redirect(url_for('jobposts')) 

@app.route('/deleteuser', methods = ['POST'])
@login_required
def deleteuser():
    if request.method == 'POST':
        user = Users.query.filter_by(id = current_user.id).first()
        db.session.delete(user)
        
        saved_by_user = Savedjobs.query.filter_by(user_id = current_user.id)
        for job in saved_by_user:
            db.session.delete(job)

        jobs_by_user = Jobs.query.filter_by(created_by = current_user.id)
        for job in jobs_by_user:
            db.session.delete(job)
            
        db.session.commit()
        logout_user()
        return redirect(url_for('index')) 

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
    jobs = Jobs.query.filter(Jobs.title.like('%' + queryterm + '%') | Jobs.description.like('%' + queryterm + '%') | Jobs.company.like('%' + queryterm + '%') | Jobs.location.like('%' + queryterm + '%'))
    return render_template('searchresults.html', jobs=jobs, searchterm=queryterm)

@app.route('/addjob', methods = ['GET','POST'])
@login_required
def addjob():
    if request.method == 'GET':   
        return render_template('addjob.html')

    if request.method == 'POST':
        

        lgbt = "lgbt" in request.form
        genderbalance = "genderbalance" in request.form
        insurance = "insurance" in request.form
        mentoring = "mentoring" in request.form
        zero_harrassment = "zero_harrassment" in request.form
        no_pay_gap = "no_pay_gap" in request.form
        diverse_interview = "diverse_interview" in request.form
        open_to_bootcamp = "open_to_bootcamp" in request.form
        open_to_career_gap = "open_to_career_gap" in request.form
        parttime = "parttime" in request.form
        fourday = "fourday" in request.form
        childcare = "childcare" in request.form
        remote_work = "remote_work" in request.form
        experience_requirements = "experience_requirements" in request.form
        flexible_hours = "flexible_hours" in request.form
        
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
                    lgbt=lgbt, 
                    genderbalance=genderbalance, 
                    insurance=insurance,
                    mentoring=mentoring, 
                    zero_harrassment=zero_harrassment, 
                    no_pay_gap=no_pay_gap,
                    diverse_interview=diverse_interview, 
                    open_to_bootcamp=open_to_bootcamp, 
                    open_to_career_gap=open_to_career_gap,
                    parttime=parttime, 
                    fourday=fourday, 
                    childcare=childcare,
                    remote_work=remote_work, 
                    experience_requirements=experience_requirements, 
                    flexible_hours=flexible_hours
        )

        db.session.add(job)
        db.session.commit()
        flash('Your job was posted.')
        return redirect(url_for('jobposts'))

@app.route('/jobposts/saved', methods = ['GET', 'POST'])
@login_required
def saved():
    if request.method == 'GET': 
        saved = Savedjobs.query.filter_by(user_id = current_user.id)
        jobs=[]
        for item in saved:
            job = Jobs.query.filter_by(job_id = item.job_id).first()
            user = Users.query.filter_by(id = job.created_by).first()
            job.username = user.name
            job.saved = 'Remove'   
            jobs.append(job)
        return render_template('jobposts.html', jobs=jobs)
      
    if request.method == 'POST': 
        if(request.args.get('option')=='add'):
            savedjobs = Savedjobs( job_id = int(request.args.get('id')), user_id = current_user.id)
            db.session.add(savedjobs)

        elif(request.args.get('option')=='remove'):
            savedjobs = Savedjobs.query.filter_by(job_id = int(request.args.get('id')), user_id = current_user.id).first()
            db.session.delete(savedjobs)

        db.session.commit()
        return ('', 204)
