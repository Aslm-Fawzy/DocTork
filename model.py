# import numpy as np
from ML_Model.API_2.PDF.Rheumatiod.rheumatiod_arthities_pdf import predict_pdf as rheumatiod_pdf
from ML_Model.API_2.Manual.Rheumatiod.rheumatiod_arthities_manual import predict_manual as rheumatiod_manual
from ML_Model.API_2.CV_ML_model_images.rheumatiod.rheumatoi_arthritis import predict_image as rheumatiod_image
from ML_Model.API_2.PDF.Prostatic.prostatic_cancer_pdf import predict_pdf as prosatic_cancer_pdf
from ML_Model.API_2.Manual.Prostatic.prostatic_cancer_manual import predict_manual as prosatic_cancer_manual
from ML_Model.API_2.CV_ML_model_images.prostatic.prostatic_cancer import predict_image as prosatic_cancer
from ML_Model.API_2.PDF.Parathyroid.parathyroid_pdf import predict_pdf as parathyroid_pdf
from ML_Model.API_2.Manual.Parathyroid.parathyroid_manual import predict_manual as parathyroid_manual
from ML_Model.API_2.CV_ML_model_images.Parathyroid.parathyroid import predict_image as parathyroid_image
from ML_Model.API_2.PDF.Diabetes.diabetes_pdf import predict_pdf as diabetes_pdf
from ML_Model.API_2.Manual.Diabetes.diabetes_manual import predict_manual as diabetes_manual
from ML_Model.API_2.CV_ML_model_images.Diabetes.diabetes import predict_image as diabetes_image
from ML_Model.API_2.PDF.Jaundice.jaundice_pdf import predict_pdf as jaundice_pdf
from ML_Model.API_2.Manual.Jaundice.juandice_manual import predict_manual as jaundice_manual
from ML_Model.API_2.CV_ML_model_images.Jaundice.jaundice import predict_image as jaundice_image
from ML_Model.API_2.PDF.Gout.gout_pdf import predict_pdf as gout_pdf
from ML_Model.API_2.Manual.Gout.gout_manual import predict_manual as gout_manual
from ML_Model.API_2.CV_ML_model_images.Gout.gout import predict_image as gout_image
from ML_Model.API_2.PDF.Thyroid.thyroid_pdf import predict_pdf as thyroid_pdf
from ML_Model.API_2.Manual.Thyroid.thyroid_manual import predict_manual as thyroid_manual
from ML_Model.API_2.CV_ML_model_images.Thyroid.thyroid import predict_image as thyroid_image
from ML_Model.API_2.PDF.Leukemia.lekumia_pdf import predict_pdf as leukemia_pdf
from ML_Model.API_2.Manual.Leukemia.lekmuia_manual import predict_manual as leukemia_manual
from ML_Model.API_2.CV_ML_model_images.leukemia.lekumia import predict_image as leukemia_image
from ML_Model.API_2.PDF.anemia.anemia_pdf import predict_pdf as anemia_pdf
from ML_Model.API_2.Manual.anemia.anemia_manual import predict_manual as anemia_manual
from ML_Model.API_2.CV_ML_model_images.Anemia.anemia import predict_image as anemia_image
from ML_Model.API_1.Disease_Symptoms_and_Tests.symptoms_features_and_lab_tests import symptoms_tests_features
# from werkzeug.security import generate_password_hash, check_password_hash
import os
from os import environ
import time
import secrets
from flask import Flask, jsonify, request
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
mail = Mail()
# ##########################################################################
# ##########################################################################
# ##########################################################################
# ##########################################################################
# ##########################################################################
# ##########################################################################
# ###########################################################################
# ###########################################################################


# # Initialize variables
app = Flask(__name__, instance_relative_config=False)
db = SQLAlchemy()

@app.route('/doctork/predict-manual', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = symptoms_tests_features(data['exp'])
    return jsonify(prediction)


@app.route('/anemia-photo', methods=['POST'])
def upload_photo():

    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = anemia_image(file_location)
    return jsonify(prediction), 201


@app.route('/anemia-manual', methods=['POST'])
def enter_anemia_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = anemia_manual(values)
    return jsonify(prediction)


@app.route('/anemia-pdf', methods=['POST'])
def upload_anemia_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = anemia_pdf(file_location)
    return jsonify(prediction), 201
##########################################################################


@app.route('/leukemia-photo', methods=['POST'])
def upload_photo_leukemia():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = leukemia_image(file_location)
    return jsonify(prediction), 201


@app.route('/leukemia-manual', methods=['POST'])
def enter_leukemia_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = leukemia_manual(values)
    return jsonify(prediction)


@app.route('/leukemia-pdf', methods=['POST'])
def upload_leukemia_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = leukemia_pdf(file_location)
    return jsonify(prediction), 201
##########################################################################


@app.route('/thyroid-photo', methods=['POST'])
def upload_photo_thyroid():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = thyroid_image(file_location)
    return jsonify(prediction), 201


@app.route('/thyroid-manual', methods=['POST'])
def enter_thyroid_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = thyroid_manual(values)
    return jsonify(prediction)


@app.route('/thyroid-pdf', methods=['POST'])
def upload_thyroid_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = thyroid_pdf(file_location)
    return jsonify(prediction), 201

##########################################################################


@app.route('/gout-photo', methods=['POST'])
def upload_photo_gout():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = gout_image(file_location)
    return jsonify(prediction), 201


@app.route('/gout-manual', methods=['POST'])
def enter_gout_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = gout_manual(values)
    return jsonify(prediction)


@app.route('/gout-pdf', methods=['POST'])
def upload_gout_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = gout_pdf(file_location)
    return jsonify(prediction), 201

##########################################################################


@app.route('/jaundice-photo', methods=['POST'])
def upload_photo_jaundice():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = jaundice_image(file_location)
    return jsonify(prediction), 201


@app.route('/jaundice-manual', methods=['POST'])
def enter_jaundice_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = jaundice_manual(values)
    return jsonify(prediction)


@app.route('/jaundice-pdf', methods=['POST'])
def upload_jaundice_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = jaundice_pdf(file_location)
    return jsonify(prediction), 201

##########################################################################


@app.route('/diabetes-photo', methods=['POST'])
def upload_photo_diabetes():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = diabetes_image(file_location)
    return jsonify(prediction), 201


@app.route('/diabetes-manual', methods=['POST'])
def enter_diabetes_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = diabetes_manual(values)
    return jsonify(prediction)


@app.route('/diabetes-pdf', methods=['POST'])
def upload_diabetes_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = diabetes_pdf(file_location)
    return jsonify(prediction), 201

##########################################################################


@app.route('/parathyroid-photo', methods=['POST'])
def upload_photo_parathyroid():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = parathyroid_image(file_location)
    return jsonify(prediction), 201


@app.route('/parathyroid-manual', methods=['POST'])
def enter_parathyroid_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = parathyroid_manual(values)
    return jsonify(prediction)


@app.route('/parathyroid-pdf', methods=['POST'])
def upload_parathyroid_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = parathyroid_pdf(file_location)
    return jsonify(prediction), 201
##########################################################################


@app.route('/prosatic-photo', methods=['POST'])
def upload_photo_prosatic():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = prosatic_cancer(file_location)
    return jsonify(prediction), 201


@app.route('/prostatic-manual', methods=['POST'])
def enter_prosatic_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = prosatic_cancer_manual(values)
    return jsonify(prediction)


@app.route('/prostatic-pdf', methods=['POST'])
def upload_prosatic_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = prosatic_cancer_pdf(file_location)
    return jsonify(prediction), 201

##########################################################################


@app.route('/rheumatiod-photo', methods=['POST'])
def upload_photo_rheumatiod():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = rheumatiod_image(file_location)
    return jsonify(prediction), 201


@app.route('/rheumatiod-manual', methods=['POST'])
def enter_rheumatiod_manual():
    data = request.get_json(force=True)
    values = list(data.values())
    prediction = rheumatiod_manual(values)
    return jsonify(prediction)


@app.route('/rheumatiod-pdf', methods=['POST'])
def upload_rheumatiod_pdf():
    if 'file' not in request.files:
        return jsonify({'message': 'No file uploaded'}), 400
    f = request.files['file']
    filename, extension = f.filename.split(".")
    generated_filename = secrets.token_hex(10) + f".{extension}"
    if f.filename == '':
        return jsonify({'message': 'No file uploaded'}), 400
    file_location = os.path.join('uploads', generated_filename)
    f.save(file_location)
    prediction = rheumatiod_pdf(file_location)
    return jsonify(prediction), 201


def create_app():
    """Construct the core application."""
    mail = Mail(app)

    # This is the configuration for the email server.
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = 465
    app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_HOST_USER")
    app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_HOST_PASSWORD")
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True

    mail = Mail(app)

    app.config.from_object("config.Config")

    api = Api(app=app)
    from users.routes import create_authentication_routes
    create_authentication_routes(api=api)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
