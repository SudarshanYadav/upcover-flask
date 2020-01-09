from flask import Flask

app = Flask(__name__)

import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier


@app.route('/')
def quote():
    from sklearn.externals import joblib
    m = joblib.load('insurance_premium_predictor.pkl')
    prediction = m.predict([[2163, 22, 100, 100]])
    return "%d"%prediction


if __name__ == '__main__':
    app.run(host='0.0.0.0')