chapter 3 of Practical MLOps: Operationalizing Machine Learning Models by Noah Gift

==============================

Last training in dev enviroment:
* Date: 04-17-2022

----------------------

## Objetives

This mini project aims to build a machine learning API using Flask. This project aims to consolidate my recently acquired knowledge on Flask, Docker and MLops practices such as Makefile usage.  

This service returns a float number indicating the value of the house given certain features.

API request could be either POST or GET methods. 

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

* POST and GET method client request to the server

`python predict_get.py`

`python predict_post.py`

it should return something like 

{
  "prediction": [
    20.353731771344123
  ]
}

and voilá! 

## Python
Using Python 3.7.

## Project organization 

    ├── Makefile           <- Makefile with commands like `make install`
    ├── requirements       
    ├── README.md   
    ├── Dockerfile             
    ├── main.yaml          <- yaml file for AWS CodeBuild service test
    ├── notebook           <- Folder for Jupyter notebook for ML service and model dump
    │   ├── boston_housing_pickle.ipynb         <- notebook for model train and dump
    │   ├── boston_housing_prediction.joblib    <- dumped model
    │   ├── housing.csv                         <- data source
    ├── webapp             <- Folder for the API ML 
    │   ├── app.py                                     <- service in flask
    │   ├── boston_housing_prediction.joblib           <- dumped model
    │   ├── predict_get.py                             <- request using GET method for test
    │   ├── predict_post.py                            <- request using POST method for test