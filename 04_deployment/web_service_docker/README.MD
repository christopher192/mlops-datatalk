
# Deployment

## <ins>Introduction</ins>
In this section, it is the process of deploying a machine learning model as a web service.
- Creating a virtual environment with Pipenv
- Creating a script for predictiong
- Putting the script into a Flask app
- Packaging the app to Docker

## <ins>Command-line Interface</ins>
```
pip freeze
pip freeze > requirements.txt
pip freeze | grep scikit-learn
```
```
pip install pipenv
pipenv --python 3.11.8
pipenv install scikit-learn flask gunicorn
pipenv install --dev requests
```
Docker image
```
docker all images
docker rmi <image-id-or-name>
docker rmi $(docker images -q)
```
Docker container
```
docker ps -a
docker rm $(docker ps -a -q)
docker rm -f $(docker ps -a -q)
```
Build Docker image `.` mean current directory
```
docker build -t ride-duration-prediction-service:v1 .
```
Run Docker container
```
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```