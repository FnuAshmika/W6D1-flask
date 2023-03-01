from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, LoginForm, BlogForm, CarForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CarForm()
    if form.validate_on_submit():
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
        flash(f'Successfully logged in!!')  
        return redirect('/')
    return render_template('login.jinja', login_form = form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Request to sign-up {form.username} successful!')
        return redirect('/')
    return render_template('register.jinja', form=form)



 