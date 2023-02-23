FROM BREAK THE DOCKERFILE SO PIPELINE FAILS
COPY app /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD [ "python", "app.py" ]