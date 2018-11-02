from flask import Flask, render_template, request, url_for
from flask_login import login_user, current_user, login_required, logout_user, login_manager, LoginManager, UserMixin
from flask_mongoengine import MongoEngine
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "ivr-project"}
'''ivr-project'''
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)


register_blueprints(app)


class User(UserMixin, db.Document):
    email = db.StringField(max_length=30)
    password = db.StringField()
    class_number = db.StringField(max_length=10)
    purpose = db.StringField()


@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()


class RegForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])
    class_number = StringField('class_number', validators=[InputRequired(), Length(max=10)])
    purpose = StringField('purpose', validators=[InputRequired(), Length(max=100)])


class RegForm1(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=20)])


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if request.method == 'POST':
        if form.validate():
            existing_user = User.objects(email=form.email.data).first()
            if existing_user is None:
                hashpass = generate_password_hash(form.password.data, method='sha256')
                hey = User(form.email.data, hashpass, form.class_number.data, form.purpose.data).save()
                login_user(hey)
                return redirect(url_for('dashboard'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = RegForm1()
    if request.method == 'POST':
        if form.validate():
            check_user = User.objects(email=form.email.data).first()
            if check_user:
                if check_password_hash(check_user['password'], form.password.data):
                    login_user(check_user)
                    return redirect(url_for('posts.list'))
    return render_template('login.html', form=form)


@app.route('/logout', methods = ['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.email)


if __name__ == '__main__':
    app.run()
