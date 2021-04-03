# Breast Cancer Prediction


## Attribute Information:
```
1. Sample code number: ID number
2. Clump Thickness:1-10
3. Uniformity of Cell size:1-10
4. Uniformity of Cell shape:1-10
6. Marginal Adhesion:1-10
7. Single Epithelial Cell Size:1-10
8. Bare Nuclei:1-10
9. Bland Chromatin:1-10
10. Normal Nucleoli:1-10
11. Mitoses:1-10
12. Class: (2 for Benign, 4 for Malignant)
```

## Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

• Now, You should be able to view the homepage

• Enter valid numerical values in all input boxes and hit Predict.

• If everything goes well, you should  be able to see the cancer prediction on the HTML page!

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
