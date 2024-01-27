import joblib
import pandas as pd
import numpy as np
import sklearn


loaded_model = joblib.load('random_forest_model.joblib')
num_pipeline = joblib.load('num_pipeline.joblib')
cat_pipeline = joblib.load('categorical_pipeline.joblib')


def make_prediction_motherfucker(AIRLINE, AIRLINE_CODE, ORIGIN, ORIGIN_CITY, DEST, DEST_CITY, CRS_DEP_TIME, CRS_ARR_TIME, DISTANCE, FL_DAY,FL_MONTH, FL_YEAR):
    data = {
        "AIRLINE": AIRLINE,
        "AIRLINE_CODE": AIRLINE_CODE,
        "ORIGIN": ORIGIN,
        "ORIGIN_CITY": ORIGIN_CITY,
        "DEST": DEST,
        "DEST_CITY": DEST_CITY,
        "CRS_DEP_TIME": CRS_DEP_TIME,
        "CRS_ARR_TIME": CRS_ARR_TIME,
        "DISTANCE": DISTANCE,
        "FL_DAY": FL_DAY,
        "FL_MONTH": FL_MONTH,
        "FL_YEAR": FL_YEAR
    }
    data = pd.DataFrame([data])

    data_num = data.select_dtypes(include=[np.number])
    data_cat = data.select_dtypes(exclude=[np.number])

    data_num_transformed = num_pipeline.transform(data_num)
    data_cat_transformed = cat_pipeline.transform(data_cat)

    num_columns = data_num.columns.drop('DISTANCE')

    data_num_transformed_df = pd.DataFrame(data=data_num_transformed, columns=list(num_columns) + ['LOG_DISTANCE'])
    data_cat_transformed_df = pd.DataFrame(data=data_cat_transformed, columns=data_cat.columns)

    data = data_cat_transformed_df.join(data_num_transformed_df)

    result = loaded_model.predict(data)
    print(data)
    print(result)

    return result[0]