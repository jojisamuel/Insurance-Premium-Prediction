from flask import Flask, render_template, request
import os
import numpy as np
from mlProject.pipeline.prediction import PredictionPipeline
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)  # initializing a flask app

@app.route('/', methods=['GET'])  # route to display the home page
def home_page():
    return render_template("index.html")

@app.route('/train', methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful!" 

@app.route('/predict', methods=['POST', 'GET'])  # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            # Reading user inputs and converting to appropriate data types
            age = float(request.form["age"])
            sex = request.form["sex"]
            bmi = float(request.form["bmi"])
            children = float(request.form["children"])
            smoker = request.form["smoker"]
            region = request.form["region"]

            # Create a dictionary for the data
            data = {
                'age': age,
                'sex': sex,
                'bmi': bmi,
                'children': children,
                'smoker': smoker,
                'region': region
            }

            # Use label encoders on categorical variables
            label_encoder = LabelEncoder()
            data['sex'] = label_encoder.fit_transform([data['sex']])[0]
            data['smoker'] = label_encoder.fit_transform([data['smoker']])[0]
            data['region'] = label_encoder.fit_transform([data['region']])[0]

            # You can now convert the dictionary to a list if needed
            data_list = [data[key] for key in ['age', 'sex', 'bmi', 'children', 'smoker', 'region']]
            data_array = np.array(data_list).reshape(1, -1)

            print(data_array)
            
            obj = PredictionPipeline()
            predict = obj.predict(data_array)

            return render_template('index.html', prediction=predict)

        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
