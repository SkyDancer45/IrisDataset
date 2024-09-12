import joblib
from flask import Flask, request, url_for, render_template
import os
import subprocess
from flask import  request, jsonify


import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
import numpy as np
from sklearn.svm import SVC

# Load your model using joblib
model = joblib.load('../Cowabunga.sav')  # Replace with your model path

# ... (rest of your Flask application code)
app = Flask(__name__, template_folder='./templates/')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():

  # Get the input data from the POST request
    data = request.get_json()
    # Extract the feature data
    feature_data = [
            float(data['sepal_length']),
            float(data['sepal_width']),
            float(data['petal_length']),
            float(data['petal_width'])
        ]
    # Reshape the data to a 2D array
    reshaped_data = np.array(feature_data).reshape(1, -1)
    reshaped_data = reshaped_data.astype(float)
    # Make the prediction using the loaded model
    prediction = model.predict(reshaped_data)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction.tolist()})

if __name__ == "__main__":
  app.run(debug=True)




