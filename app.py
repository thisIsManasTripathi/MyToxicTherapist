from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def processChat():
    data = request.get_json()
    print(data)
    return {"reply": "idkwhatever"}

@app.route("/", methods=['GET'])
def Home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)