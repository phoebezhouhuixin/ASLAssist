# ASLAssist


ASLAssist aims to aid the deaf-mute towards a completely wireless platform by converting American Sign Language to a text form. It can be used as a web chat for the deaf-mute.

# Getting Started

First, train the model using Train_CNN. After this step you will obtain a file with the trained model, called "my_model.h5". You may use the Predict_one_image file to test the accuracy of the model.

Next, create a folder called 'pictures' in the place where you have downloaded all the code. We first run webcam.py to open the webcam and take the pictures of your ASL signs. Click c to keep taking more pictures, and q twice to stop the webcam and to close all windows. 

Next, put the file "image.html" into a new folder called templates. Then, run "model.py". model.py integrates the model with some front end features. model.py causes a localhost server to be set up. Open the localhost server in order to see the interface that is encoded by image.html.

# Installations
On windows open command prompt centre and run the codes beginning with pip.requires python 3.7
Tensorflow
pip install tensorflow
keras
pip install keras
PIL
pip install Pillow==2.2.1
flask
pip install flask
Socketio
pip install flask-socketio
pandas
pip install pandas
numpy
pip install numpy
