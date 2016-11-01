FROM python:3-alpine
EXPOSE 8081
COPY requires.txt /tmp
RUN pip install --timeout 60 -r /tmp/requires.txt
WORKDIR /application
CMD gunicorn -c gunicorn.cfg manage:app
