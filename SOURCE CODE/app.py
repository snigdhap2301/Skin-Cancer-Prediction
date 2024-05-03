from flask import Flask, render_template, request
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore
from tensorflow.keras.preprocessing import image # type: ignore
from tensorflow.keras.metrics import AUC # type: ignore
import numpy as np

app = Flask(__name__)

dependencies = {
    'auc_roc': AUC
}

verbose_name = {
0: 'Actinic keratoses and intraepithelial carcinomae',
1: 'Basal cell carcinoma',
2: 'Benign keratosis-like lesions',
3: 'Dermatofibroma',
4: 'Melanocytic nevi',
5: 'Pyogenic granulomas and hemorrhage',
6: 'Melanoma',

           }




model = load_model('D:\Skin Cancer Prediction\SOURCE CODE\model\skin.h5')

def predict_label(img_path):
	test_image = image.load_img(img_path, target_size=(28,28))
	test_image = image.img_to_array(test_image)/255.0
	test_image = test_image.reshape(1, 28,28,3)

	predict_x=model.predict(test_image) 
	classes_x=np.argmax(predict_x,axis=1)
	
	return verbose_name[classes_x[0]]

 
@app.route("/")
@app.route("/first")
def first():
	return render_template('first.html')
    
@app.route("/login")
def login():
	return render_template('login.html')   
    
@app.route("/index", methods=['GET', 'POST'])
def index():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "D:/Skin Cancer Prediction/SOURCE CODE/static/tests/" + img.filename	
		img.save(img_path)

		predict_result = predict_label(img_path)

	return render_template("prediction.html", prediction = predict_result, img_path = img_path)

 
    


	
if __name__ =='__main__':
	app.run(debug = True)