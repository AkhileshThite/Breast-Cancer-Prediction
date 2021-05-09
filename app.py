"""

Created on March 21 2021
@author: Akhilesh Thite

"""

# Importing necessary libraries.
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

# Defining Flask app
app = Flask(__name__)
# Loading the trained ML model in pickle file
model = pickle.load(open('model.pkl', 'rb'))


# This will head us to the main index.html file.
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])
def predict():
    # Converting the multiple inputs into numpy array
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]

    # Tumor columns in dataset
    features_name = ['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
                     'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
                     'bland_chromatin', 'normal_nucleoli', 'mitoses']

    # Predicting the input values
    df = pd.DataFrame(final_features, columns=features_name)
    output = model.predict(df)

    if output == 4:
        output = "Malignant tumor: You have cancer."
    else:
        output = "Benign tumor: You don't have cancer."

    return render_template('index.html', prediction=f'{output}')


# Tumor information page
@app.route("/inputs")
def inputs():
    return render_template('tumor.html')


# Hospitals google map page
@app.route("/hospitals")
def hospitals():
    return render_template('hospitals.html')


# To run the Flask app on local host.
if __name__ == "__main__":
    app.run(debug=True)
