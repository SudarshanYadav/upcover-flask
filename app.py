from flask import Flask
from flask import request
app = Flask(__name__)

import numpy as np
import pandas as pd
import json
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.externals import joblib

import pre_processing.py


@app.route('/getQuote', methods = ['POST', 'GET'])
def get_quote():
    params = request.form
    
    suburb = params.get('suburb', 'Pymble') 
    number_of_claims = params.get('numberOfClaims', 3)
    birth_year = params.get('birth_year', 8) 
    age_at_licence = params.get('ageAtLicence', 21)

    pred_params = proc_param(suburb,number_of_claims,birth_year,age_at_licence)
    
    comprehensive_quote = m_comprehensive.predict([pred_params])
    theft_quote = m_TPT.predict([pred_params])
    
    response_data = {}
    response_data['Comprehensive'] = '%f'%comprehensive_quote
    response_data['ThirdpartyTheft'] = '%f'%theft_quote
    
    print(response_data)
    return json.dumps(response_data)


if __name__ == '__main__':
    comprehensive_model = 'models/insurance_comprehensive.pkl'
    tpt_model = 'models/insurance_tpt.pkl'
    m_comprehensive = joblib.load(comprehensive_model)
    m_TPT = joblib.load(comprehensive_model)
    app.run(debug=True, host='0.0.0.0')