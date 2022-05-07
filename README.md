chapter 3 of Practical MLOps: Operationalizing Machine Learning Models by Noah Gift

==============================

Last training in dev enviroment:
* Date: 05-07-2022

----------------------

## Objetives

This mini project aims to build a machine learning API using Flask.


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

`docker build --build-arg VERSION=0.0.1 -t boston-flask-predict .`

* sping the container

`docker run -p 5000:5000 -d --name boston-flask-predict boston-flask-predict`

## Python
Using Python 3.8.1

## Project organization 

    ├── Makefile           <- Makefile with commands like `make install`
    ├── requirements       
    ├── README.md   
    ├── Dockerfile             
    ├── main.yaml          <- yaml file for AWS CodeBuild service test
    ├── notebook           <- Folder for Jupyter notebook for ML service and model dump
    │   ├── img_classification_pet.ipynb        <- notebook for model train and dump
    │   ├── img_classification_potholes.ipynb   <- notebook for model train and dump
    │   ├── model_pet.h5                        <- dumped model for pet (cat or dog classification)
    │   ├── Petimages                           <- data source for pets
    │   ├── Potholes                            <- data source for potholes
    ├── webapp             <- Folder for the API ML 
    │   ├── app.py                                     <- service in flask
    │   ├── model_pet.h3                               <- dumped model for pets
    │   ├── uploads                              <- folder responsible for receiving uploaded images from the template
    │   ├── templates                            <- html home page