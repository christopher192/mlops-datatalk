# setup official python
FROM python:3.11.8

# update pip to the latest version
RUN pip install -U pip
# unstall pipenv for managing dependencies
RUN pip install pipenv 

# set the working directory to /app
WORKDIR /app

# copy Pipfile and Pipfile.lock to the Docker image
# "./" -> /app
COPY [ "Pipfile", "Pipfile.lock", "./" ]

# install the Python dependencies
RUN pipenv install --system --deploy

# copy the application files to the Docker image
COPY [ "predict.py", "lin_reg.bin", "./" ]

# inform Docker that the container will listen on the specified port at runtime
EXPOSE 9696

# the command to run when the container starts
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]