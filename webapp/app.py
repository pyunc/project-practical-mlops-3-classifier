from concurrent.futures import thread
from flask import Flask, request, jsonify, send_from_directory, render_template
from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import tensorflow as tf
import os
from werkzeug.utils import secure_filename

import logging
log = logging.getLogger(__name__)
app = Flask(__name__)

IMAGE_SIZE = (180, 180)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    # return render_template('home.html', label='', imagesource='file://null')
    return render_template('home.html', label='', imagesource='')


def predict(file):

    img = load_img(file, target_size=IMAGE_SIZE)

    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    loaded_model = load_model('model_pet.h5')
    predictions = loaded_model.predict(img_array)

    score = predictions[0]

    # return {'prediction': score}
    return "This image is %.2f percent cat and %.2f percent dog." % (100 * (1 - score), 100 * score)


@app.route("/", methods=['POST', 'GET'])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        output = predict(file_path)

        return render_template(
            "home.html",
            label=output,
            imagesource=file_path)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    app.run(debug=True, threaded=False)
