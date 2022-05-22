import logging
import os

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from flask import Flask, render_template, request, send_from_directory
from keras.models import load_model
from keras.utils.image_utils import img_to_array, load_img
from lime import lime_image
from tensorflow import keras
from werkzeug.utils import secure_filename

log = logging.getLogger(__name__)
app = Flask(__name__)

IMAGE_SIZE = (180, 180)
UPLOAD_FOLDER = 'uploads'
seed = 42
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('home.html', label='', imagesource='')


def add_example(x):
    return x+1


def get_model(model: str):
    return load_model(model)


def preprocess(file_path):

    img = load_img(file_path, target_size=IMAGE_SIZE)
    img_array = img_to_array(img)
    tf_img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    np_img_array = np.expand_dims(img_array, axis=0)

    return tf_img_array, np_img_array


def evaluate(model, np_img_array, file_path):

    explainer = lime_image.LimeImageExplainer()

    explanation = explainer.explain_instance(
        np_img_array[0].astype('double'),
        model.predict,
        top_labels=3,
        hide_color=None,
        num_samples=500
    )

    _, mask_1 = explanation.get_image_and_mask(
        explanation.top_labels[1],
        positive_only=True,
        num_features=3,
        hide_rest=True
    )

    # get the file from the folder
    img = keras.preprocessing.image.load_img(file_path, target_size=IMAGE_SIZE)

    _, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(100, 100))

    ax1.imshow(img, alpha=0.7)
    ax2.imshow(mask_1, alpha=0.7)
    ax3.imshow(img, alpha=0.7)
    ax3.imshow(mask_1, alpha=0.5)
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')

    # upload new file to the uploads

    filename_explained = file_path.split('/')[-1]

    filename_explained = f'explained_{filename_explained}'

    filename_explained_path = os.path.join(
        app.config['UPLOAD_FOLDER'],
        filename_explained
    )

    plt.savefig(f'{filename_explained_path}', transparent=True)

    return f'{filename_explained_path}'


def predict(model, tf_img_array):
    predictions = model.predict(tf_img_array)
    score = [float(x) for x in predictions[0]]

    return "This image is {:.0%} cats, {:.0%} dogs and {:.0%} potholes".format(score[0], score[1], score[3])


@app.route("/", methods=['POST', 'GET'])
def upload_file():

    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        print('file_path ', file_path)  # file_path  uploads/21.jpg
        file.save(file_path)

        loaded_model = get_model('model.h5')

        tf_img_array, np_img_array = preprocess(file_path)

        output_predict = predict(
            model=loaded_model,
            tf_img_array=tf_img_array
        )

        output_explanation_path = evaluate(
            model=loaded_model,
            np_img_array=np_img_array,
            file_path=file_path
        )

        print(f'output_explanation_path {output_explanation_path}')

        return render_template(
            "home.html",
            label=output_predict,
            imagesource=output_explanation_path)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, threaded=False, port=port, host='0.0.0.0')
    # app.run(debug=True, threaded=False)
