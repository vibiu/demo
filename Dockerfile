FROM python:3
COPY requires.txt /tmp/
RUN pip install -r /tmp/requires.txt -i https://pypi.douban.com/simple
EXPOSE 8000
WORKDIR /app
CMD ["python", "manage.py"]
