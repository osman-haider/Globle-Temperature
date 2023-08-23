from flask import Flask,request,jsonify
import pickle
import pandas as pd
import numpy as np
import sklearn


model = pickle.load(open('globle_temp.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/predict', methods=['POST'])
def crop():
    Latitude_value = float(request.form.get('Latitude_value'))
    Longitude_value = float(request.form.get('Longitude_value'))
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))
    day = int(request.form.get('day'))
    Latitude_direction = request.form.get('Latitude_direction_N_or_S')
    Longitude_direction = request.form.get('Longitude_direction_E_or_W')

    Latitude_direction_numric = None
    Longitude_direction_numric = None

    if(Latitude_direction=="N"):
        Latitude_direction_numric=0
    elif(Latitude_direction == "S"):
        Latitude_direction_numric=1

    if(Longitude_direction == "E"):
        Longitude_direction_numric = 0
    elif(Longitude_direction == "W"):
        Longitude_direction_numric= 1

    data = np.array([[Latitude_value, Longitude_value, year, month, day, Latitude_direction_numric,Longitude_direction_numric]])

    result = model.predict(data)[0]

    result_list =result.tolist()

    return jsonify({'Temperature in your area': result_list})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
    #app.run(debug=True)