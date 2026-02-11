from flask import Flask, request, jsonify
import sys
sys.path.insert(0, "model") 
from flask_cors import CORS
from model import findSentimentIndex, respond

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def processChat():
    data = request.get_json()
    filteredData = data['message'].split(".")
    response = respond(findSentimentIndex(filteredData))
    return {"reply": response}

@app.route("/", methods=['GET'])
def Home():
    return 0

if __name__ == '__main__':
    app.run(debug=True)