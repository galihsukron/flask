# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.5
COPY . /opt/flask
WORKDIR /opt/flask
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["flask-server.py"]
