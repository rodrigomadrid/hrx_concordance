from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello, DevOps world!"})

if __name__ == "__main__":
    app.run(debug=True)
