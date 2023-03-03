from . import bp as auth_bp
from flask import render_template, flash, redirect
from app.forms import RegisterForm, LoginForm
from app.blueprints.social.models import User
from flask_login import current_user, login_user, logout_user, login_required

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email= form.email.data
        password= form.password.data
        user_match = User.query.filter_by(email=email).first()
        if not user_match or not user_match.verify_password(password):
            flash(f'Username or Password incorrect. Try again!!!')
            return redirect('/auth/login')

        flash(f'{form.email.data} successfully signed in!!')
        login_user(user_match, remember=form.remember_me.data)
        return redirect('/')
    return render_template('login.jinja', login_form = form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username=form.username.data
        email=form.email.data
        password=form.password.data
        firstname=form.firstname.data
        lastname= form.lastname.data
        u= User(username=username, email=email,first_name=firstname, last_name=lastname, password_hash='')
        user_match = User.query.filter_by(username=username).first()
        email_match = User.query.filter_by(email=email).first()
        if user_match:
            flash(f'Username {username} already exist. Try again!!')
            return redirect('/auth/register')
        elif email_match:
            flash(f'Email {email} already exist. Try again!!')
            return redirect('/auth/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful!')
            return redirect('/')
        
    return render_template('register.jinja', form=form)

@auth_bp.route('/signout')
@login_required
def sign_out():
    logout_user()
    return redirect('/')
