# Pull python3 image
FROM python:3.8-slim-buster

# Set work directory
WORKDIR /owapi

# Copy requirements file to the image
COPY requirements.txt requirements.txt

# Set flask app location
ENV FLASK_APP=owapi/app

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy all the content from the local folder to the image
COPY . .

# Run flask application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]