from flask import Flask
from flask import request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Hi, You need to send the params. Thanks!"


@app.route("/api", methods=['GET', 'POST'])
def api():

    n1 = request.args.get('n1')
    n2 = request.args.get('n2')

    theValues = [int(n1), int(n2)]

    c1 = int(n1) * int(n1)
    c2 = int(n2) * int(n2)
    c3 = int(c1) + int(c2)
    c4 = pow(c3, 0.5)

    sumResult = sum(theValues)

    return {'sum': sumResult}
    # return {'sum': c4}


# Debug Mode True
if __name__ == "__main__":
    app.run(debug=True)
