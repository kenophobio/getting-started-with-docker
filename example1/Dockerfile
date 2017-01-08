# getting-started-with-docker/example1/Dockerfile
FROM python:3.6-alpine

# Install python dependencies
ADD ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy the source code to /opt/example1
ADD . /opt/example1/

# Run!
WORKDIR /opt/example1
CMD ["python", "example1.py"]