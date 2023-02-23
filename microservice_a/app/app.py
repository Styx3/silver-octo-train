from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def response():
    return jsonify(
        microservice_a=["Hello", "World"],
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='8080')