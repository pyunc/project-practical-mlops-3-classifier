chapter 3 of Practical MLOps: Operationalizing Machine Learning Models by Noah Gift

==============================

track:

Solution able to Dockerized:
* Date: 05-15-2022

Last training in dev enviroment:
* Date: 05-07-2022

----------------------

## Objetives

This mini classifier project aims to build a machine learning API using Flask and Docker. 




inspired by this amazing github:

- https://github.com/mitkir/keras-flask-image-classifier
- https://github.com/utk-ink/Defect-Detection-of-PCB

## Initial setup or MakeFile

python -m venv .env
source .env/bin/activate
pip install -U pip
pip install -r requirements.txt

**or** 

`make install`

## Docker 

* build image

`docker image build --build-arg VERSION=0.0.1 -t image_classifier .`

* spin the container

`docker run -d -p 5000:5000 -d image_classifier`

* open in a browser 

`http://localhost:5000/`

## Python
Using Python 3.8.1

## Project organization 

    ├── Makefile           <- Makefile with commands like `make install`
    ├── requirements       
    ├── README.md   
    ├── Dockerfile             
    ├── main.yaml                               <- yaml file for AWS CodeBuild service test
    ├── notebook                                 <- Folder for Jupyter notebook for ML service and model dump
    │   ├── img_classification_potholes.ipynb    <- notebook for model train and dump
    │   ├── pothole_10.h5                        <- dumped model for pet (cat or dog classification)
    │   ├── ImagesPotholes                       <- data source for potholes
    ├── webapp                                   <- Folder for the API ML 
    │   ├── app.py                               <- service in flask
    │   ├── model.h3                             <- dumped model for pets
    │   ├── uploads                              <- folder responsible for receiving uploaded images from the template
    │   ├── templates                            <- html home page