# Container image that runs your code
FROM python:3.8.0

# Install jq
RUN apt-get update && apt-get install jq -y

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt
COPY fix.py /fix.py

# Install requirements
RUN pip install -r /requirements.txt

# Code file to execute when the docker container starts up (`entrypoint.sh`)
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
