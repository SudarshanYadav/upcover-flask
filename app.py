from flask import Flask
from flask import request
app = Flask(__name__)

import numpy as np
import pandas as pd
import json
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier


@app.route('/')
def quote():
    from sklearn.externals import joblib
    m = joblib.load('insurance_premium_predictor.pkl')
    prediction = m.predict([[2163, 22, 100, 100]])
    return "%d"%prediction

@app.route('/getQuote', methods = ['POST'])
def get_quote():
    from sklearn.externals import joblib
    m = joblib.load('insurance_premium_predictor.pkl')
    params = json.load(request.data)
    postcode = params.get('postalcode', '2163')
    year = params.get('year', 1992)
    day = params.get('day', 6)
    month = params.get('month', 8)
    age_at_licence = params.get('ageAtLicence', 21)
    number_of_claims = params.get('numberOfClaims', 3)
    
    comprehensive_quote = m.predict([[postcode, 22, age_at_licence, number_of_claims]])
    theft_quote = m.predict([[postcode, 91, age_at_licence, number_of_claims]])
    response_data = {}
    response_data['Comprehensive'] = '%f'%comprehensive_quote
    response_data['ThirdpartyTheft'] = '%f'%theft_quote
    print(response_data)
    return json.dumps(response_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')