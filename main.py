from flask import Flask, jsonify, json
from fetch_uv_data import fetch_uv_data

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h1>Hello from {name}!</h1>\nGoto /api to fetch UV data".format(name="Mehwish") 
    return html

@app.route("/api", methods=['GET'])
def get_uv_data():
    uv = fetch_uv_data()
    return jsonify(uv)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
