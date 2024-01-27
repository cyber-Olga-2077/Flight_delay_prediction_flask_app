from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import FunctionTransformer
import numpy as np


class CombinedAttrs(BaseEstimator, TransformerMixin):   #klasa transformacji
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        log_transformer = FunctionTransformer(np.log, inverse_func=np.exp)
        LOG_DISTANCE = log_transformer.transform(X[:, 3])
        X = np.delete(X, 3, axis=1)

        return np.c_[X, LOG_DISTANCE]
