import flask
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import math

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    features = {}
    features['university'] = request.form['university']
    features['district'] = request.form['district']
    features['level'] = request.form['level']
    features['language'] = request.form['language']
    features['accomodation_covered'] = int(request.form['accomodation_covered'])
    features['living_expense_covered'] = int(request.form['living_expense_covered'])
    features['start_month'] = request.form['start_month']
    features['start_year'] = int(request.form['start_year'])
    prediction = model.predict(pd.DataFrame([features]))
    output = math.ceil(prediction[0])

    return render_template('index.html', prediction=output)

@app.route('/results',methods=['POST'])
def results():

    features = {}
    features['university'] = request.form['university']
    features['district'] = request.form['district']
    features['level'] = request.form['level']
    features['language'] = request.form['language']
    features['accomodation_covered'] = int(request.form['accomodation_covered'])
    features['living_expense_covered'] = int(request.form['living_expense_covered'])
    features['start_month'] = request.form['start_month']
    features['start_year'] = int(request.form['start_year'])
    prediction = model.predict([features])
    


    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
