from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app.util import get_city_from_airport, calculate_dist_between_airports


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fligh-Seeker'}
    posts = [
        {
            'author': {'username': 'Olga'},
            'body': 'Beautiful day in Poland! joking'
        },
        {
            'author': {'username': ' Better Olga'},
            'body': 'The Avengers movie was so cool! not really though'
        }
    ]
    return render_template('index.html',  user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        FL_DATE = form.date.data
        FL_MONTH = FL_DATE.month
        ORIGIN = form.origin.data
        ORIGIN_CITY = get_city_from_airport(ORIGIN)
        DEST = form.destination.data
        DEST_CITY = get_city_from_airport(DEST)
        CRS_DEP_TIME = form.departure_time.data.hour*100 + form.departure_time.data.minute
        CRS_ARR_TIME = form.arrival_time.data.hour*100 + form.arrival_time.data.minute
        DISTANCE = calculate_dist_between_airports(ORIGIN, DEST)
    return render_template('login.html', title='Sign In', form=form)
