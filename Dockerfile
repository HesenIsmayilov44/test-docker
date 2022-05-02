FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DEBUG True
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
ADD . .

CMD [ "gunicorn", "--bind", "0.0.0.0", "-p", "8000",  "RestApi.wsgi" ]