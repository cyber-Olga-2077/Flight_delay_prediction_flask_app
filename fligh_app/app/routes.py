from app import app
from flask import render_template
from app.forms import PredictionForm
from flask import render_template, flash, redirect, url_for
from app.util import get_city_from_airport, calculate_dist_between_airports, get_airline_from_code
from app.prediction import make_prediction_motherfucker
import math

@app.route('/', defaults = {'path': ''}, methods= ["GET", "POST"])
@app.route('/<path:path>', methods= ["GET", "POST"])
def index(path):
    form = PredictionForm()

    result = None
    if form.validate_on_submit():
        AIRLINE_CODE =  form.airline.data
        AIRLINE = get_airline_from_code(AIRLINE_CODE)
        FL_DATE = form.date.data
        ORIGIN = form.origin.data
        ORIGIN_CITY = get_city_from_airport(ORIGIN)
        DEST = form.destination.data
        DEST_CITY = get_city_from_airport(DEST)
        CRS_DEP_TIME = form.departure_time.data.hour*100 + form.departure_time.data.minute
        CRS_ARR_TIME = form.arrival_time.data.hour*100 + form.arrival_time.data.minute
        DISTANCE = calculate_dist_between_airports(ORIGIN, DEST)
        FL_DAY = FL_DATE.day
        FL_MONTH = FL_DATE.month
        FL_YEAR = FL_DATE.year

        result = math.trunc(make_prediction_motherfucker(AIRLINE,AIRLINE_CODE ,ORIGIN, ORIGIN_CITY, DEST, DEST_CITY, CRS_DEP_TIME, CRS_ARR_TIME, DISTANCE, FL_DAY ,FL_MONTH, FL_YEAR))
    return render_template('index.html', form=form, result=result)
