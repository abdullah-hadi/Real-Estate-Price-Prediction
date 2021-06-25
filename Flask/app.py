from flask import Flask, jsonify,request
from util import load_file
import util
app = Flask(__name__)

@app.route('/get_location_name')
def get_location() :
    res = jsonify ({
        'location' : util.get_location()
    })
    res.headers.add('Access-Control-Alow-Origin', '*')
    return res


@app.route('/Predict_home_price', methods = ['POST'])
def price_prediction() :
    total_sqft = float(request.form(['total_sqft']))
    location = request.form(['location'])
    bhk = int(request.form(['bhk']))
    bath = int(request.form(['bath']))

    res = jsonify ({
        'estimated_price' : util.price_prediction(location, total_sqft, bhk, bath)
    })
    return res

if __name__ == '__main__' :
    print("Starting python flask server for home price prediction")
    util.load_file()
    app.run(port=5000)