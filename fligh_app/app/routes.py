from app import app
from flask import render_template
from app.forms import LoginForm
from flask import render_template, flash, redirect, url_for
from app.util import get_city_from_airport, calculate_dist_between_airports
from app.prediction import make_prediction_motherfucker
import math

@app.route('/', defaults = {'path': ''}, methods= ["GET", "POST"])
@app.route('/<path:path>', methods= ["GET", "POST"])
def index(path):
    form = LoginForm()

    result = None
    if form.validate_on_submit():
        FL_DATE = form.date.data
        ORIGIN = form.origin.data
        ORIGIN_CITY = get_city_from_airport(ORIGIN)
        DEST = form.destination.data
        DEST_CITY = get_city_from_airport(DEST)
        CRS_DEP_TIME = form.departure_time.data.hour*100 + form.departure_time.data.minute
        CRS_ARR_TIME = form.arrival_time.data.hour*100 + form.arrival_time.data.minute
        DISTANCE = calculate_dist_between_airports(ORIGIN, DEST)
        FL_MONTH = FL_DATE.month

        result = math.trunc(make_prediction_motherfucker(FL_DATE, ORIGIN, ORIGIN_CITY, DEST, DEST_CITY, CRS_DEP_TIME, CRS_ARR_TIME, DISTANCE, FL_MONTH))
    return render_template('index.html', form=form, result=result)
