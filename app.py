from flask import Flask, render_template, request, jsonify
import sys
sys.path.insert(0, "model") 
from model import findSentimentIndex, respond

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def processChat():
    data = request.get_json()
    filteredData = data['message'].split(".")
    response = respond(findSentimentIndex(filteredData))
    return {"reply": response}

@app.route("/", methods=['GET'])
def Home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)