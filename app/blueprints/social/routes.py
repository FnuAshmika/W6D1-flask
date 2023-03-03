from . import bp as social_bp
from .models import  Car, User
from app.forms import CarForm
from flask import redirect, render_template, flash
from flask_login import login_required, current_user

# @social_bp.route('/blog')
# def blog():
#     form = BlogForm()
#     return render_template('blog.jinja', blog_form=form)

@social_bp.route('/user/<username>')
def user(username):
    user_match = User.query.filter_by(username=username).first()
    if not user_match:
        redirect('/')
    cars = user_match.cars 
    return render_template('user.jinja', user=user_match, cars=cars)   



@social_bp.route('/cars', methods=['GET', 'POST'])
def cars():
    form = CarForm()
    if form.validate_on_submit():
        make= form.make.data
        model= form.model.data
        color= form.color.data
        year= form.year.data
        price= form.price.data
        c= Car(make=make, model=model, color=color, year=year, price=price, user_id=current_user.id)
        c.commit()
        flash(f'Successfully submitted!!')  
        return redirect('/social/cars')
    return render_template('cars.jinja',  car_form=form) 