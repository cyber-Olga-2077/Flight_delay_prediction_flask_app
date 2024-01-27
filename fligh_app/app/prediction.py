import joblib
import pandas as pd
import numpy as np

loaded_model = joblib.load('random_forest_model.joblib')


def make_prediction_motherfucker(FL_DATE, ORIGIN, ORIGIN_CITY, DEST, DEST_CITY, CRS_DEP_TIME, CRS_ARR_TIME, DISTANCE, FL_MONTH):
    data = {
        "FL_DATE": FL_DATE,
        "ORIGIN": ORIGIN,
        "ORIGIN_CITY": ORIGIN_CITY,
        "DEST": DEST,
        "DEST_CITY": DEST_CITY,
        "CRS_DEP_TIME": CRS_DEP_TIME,
        "CRS_ARR_TIME": CRS_ARR_TIME,
        "DISTANCE": DISTANCE,
        "FL_MONTH": FL_MONTH
    }

    required_columns = {'ARR_DELAY_STRATA', 'CRS_ARR_TIME', 'FL_MONTH', 'TAXI_IN', 'WEATHER_IMPACT', 'DEP_DELAY', 'CRS_DEP_TIME', 'DISTANCE', 'TAXI_OUT', 'AIR_TIME'}
    for col in required_columns:
        if col not in data:
            data[col] = np.nan

    columns_order = ['CRS_DEP_TIME', 'DEP_DELAY', 'TAXI_OUT', 'TAXI_IN', 'CRS_ARR_TIME',
       'AIR_TIME', 'DISTANCE', 'FL_MONTH', 'WEATHER_IMPACT',
       'ARR_DELAY_STRATA']
