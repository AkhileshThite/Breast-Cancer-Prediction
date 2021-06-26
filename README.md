# Breast Cancer Prediction Web Application
Website link: https://breast-cancer-prediction-ml.herokuapp.com

![](/static/screenshot.png)

## Attribute Information:
```
 1. clump thickness: (1-10). Benign cells tend to be grouped in monolayers, while cancerous cells are often grouped in multilayers.
 2. cell size uniformity: (1-10). Cancer cells tend to vary in size and shape. That is why these parameters are valuable in determining whether the cells are cancerous or not.
 3. cell shape uniformity: (1-10). Uniformity of cell size/shape: Cancer cells tend to vary in size and shape. That is why these parameters are valuable in determining whether the cells are cancerous or not.
 4. marginal adhesion: (1-10). Normal cells tend to stick together. Cancer cells tend to lose this ability. So the loss of adhesion is a sign of malignancy.
 5. single epithelial_cell_size: (1-10). It is related to the uniformity mentioned above. Epithelial cells that are significantly enlarged may be a malignant cell.
 6. bare nuclei: (1-10). This is a term used for nuclei not surrounded by cytoplasm (the rest of the cell). Those are typically seen in benign tumors.
 7. bland chromatin: (1-10). Describes a uniform "texture" of the nucleus seen in benign cells. In cancer cells, the chromatin tends to be more coarse.
 8. normal nucleoli: (1-10). Nucleoli are small structures seen in the nucleus. In normal cells, the nucleolus is usually very small if visible at all. In cancer cells, the nucleoli become more prominent, and sometimes there are more of them.
 9. mitoses: (1-10). Cancer is essentially a disease of uncontrolled mitosis.
    diagnose: (2 or 4). Benign (non-cancerous) or malignant (cancerous) lump in a breast.
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

3. Navigate to URL "http://localhost:5000"

• Now, You should be able to view the homepage

• Enter valid numerical values in all input boxes and hit Predict.

• If everything goes well, you should  be able to see the cancer prediction on the HTML page!

4. You can also send direct POST requests to FLask API using Python's inbuilt request module
Run the beow command to send the request with some pre-popuated values -
```
python request.py
```
