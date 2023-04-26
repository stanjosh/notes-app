# Set base image (host OS)
FROM python:3.12.0a7-slim

# By default, listen on port 5000
EXPOSE 5000/tcp

# Install any dependencies
RUN pip install -r ./notes-app/requirements.txt

# Specify the command to run on container start
CMD [ "python", "uwsgi.py" ]
