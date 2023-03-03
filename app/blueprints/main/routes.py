from . import bp as main_bp
from flask import render_template
from app.blueprints.social.models import Car


@main_bp.route('/')
def index():
    all_cars = Car.query.all()
    return render_template('index.jinja',title='Home', cars=all_cars)

@main_bp.route('/about')
def about():
    return render_template('about.jinja')