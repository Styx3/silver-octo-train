FROM break docker, fail all

COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "app.py" ]