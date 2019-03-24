# Load libraries
from flask import Flask, render_template, request, jsonify
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import io
import os
from werkzeug import secure_filename
from flask_socketio import SocketIO, emit
app = Flask(__name__)

# load the model, and pass in the custom metric function
global graph
graph = tf.get_default_graph()
model = load_model('my_model.h5')
class_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','Del','space','nothing']
model._make_predict_function()

def predict(image):
    # preprocess the image and prepare it for classification
    # resize the input image and preprocess it
    image = image.resize((64,64))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    confidence_list = model.predict(image)[0] #this [0] means get the first element in the prediction nparray
    index = np.argmax(confidence_list)
    confidence = np.amax(confidence_list)
    print(index)
    print("Predicted character: " + class_list[index],end ='\t')
    print("Predicted Confidence: ",confidence)
    return class_list[index]
 

@app.route("/")
def home():
    with open("message.txt","w") as fo:
        list = []
        for i in range(7):
            img_path = os.path.join(os.getcwd(),"images/image_" + str(i) + '.jpg')
            image = Image.open(img_path)
            character = predict(image)
            list.append(character)
        for item in list:  
            fo.write("%s " %item)  
    return render_template("index.html")


UPLOAD_FOLDER = './images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
@app.route("/upload", methods=["POST", "GET"])
def main():
    imgpaths = []
    if request.method =='POST':
        for i in range(1,6):
            file = request.files['file[]']
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
                imgpaths.append(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    
    for imgpath in imgpaths:
        predict(imgpath, model, class_list)
 
    return render_template("assistanthome.html")

# start the flask app
if __name__ == "__main__":
    app.run(debug= True, host = "0.0.0.0")
