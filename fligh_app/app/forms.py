from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TimeField, SelectField
from wtforms.validators import DataRequired
from app.util import get_airport_options, get_airline_options


class PredictionForm(FlaskForm):


    #field for the date
    date = DateField('Date', validators=[DataRequired()])
    #drop-down origin airport list
    origin = SelectField('Origin', validators=[DataRequired()], choices=get_airport_options())
    #drop-down destination airport list
    destination = SelectField('Destination', validators=[DataRequired()], choices=get_airport_options())
    #Planned departure time
    departure_time = TimeField('Departure time', validators=[DataRequired()])
    #Planned arrival time
    arrival_time = TimeField('Arrival time', validators=[DataRequired()])
    #airline
    airline = SelectField('Airline', validators=[DataRequired()], choices=get_airline_options())
    #submit button
    submit = SubmitField('Let\'s fly!')
