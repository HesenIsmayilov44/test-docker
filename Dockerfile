FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV DEBUG False
WORKDIR /code
COPY requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY ./entrypoint.sh /
ADD . .

ENTRYPOINT ["sh", "/entrypoint.sh"]