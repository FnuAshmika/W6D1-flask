from flask import render_template, flash, redirect
from app import app, db
from app.forms import RegisterForm, LoginForm, BlogForm, CarForm
from app.models import User, Car
# from flask_login import current_user, login_user

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()
    if form.validate_on_submit():
        make= form.make.data
        model= form.model.data
        color= form.color.data
        year= form.year.data
        price= form.price.data
        c= Car(make=make, model=model, color=color, year=year, price=price)
        c.commit()
        flash(f'Successfully submitted!!')  
        return redirect('/')
    return render_template('index.jinja', title='Home', car_form=form) 

@app.route('/about')
def about():
    return render_template('about.jinja')

@app.route('/blog')
def blog():
    form = BlogForm()
    return render_template('blog.jinja', blog_form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email= form.email.data
        password= form.password.data
        user_match = User.query.filter_by(email=email).first()
        if not user_match or not user_match.verify_password(password):
            flash(f'Username or Password incorrect. Try again!!!')
            return redirect('/login')

        flash(f'{form.email.data} successfully signed in!!')
        # login_user(username)
        return redirect('/')
    return render_template('login.jinja', login_form = form)

@app.route('/register', methods=['GET', 'POST'])
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
            return redirect('/register')
        elif email_match:
            flash(f'Email {email} already exist. Try again!!')
            return redirect('/register')
        else:
            u.hash_password(password)
            u.commit()
            flash(f'Request to register {username} successful!')
            return redirect('/')
        
    return render_template('register.jinja', form=form)

@app.route('/cars')
def cars():
    all_cars = Car.query.all()
    return render_template('cars.html', cars=all_cars)



 