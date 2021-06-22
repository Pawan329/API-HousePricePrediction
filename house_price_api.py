# importing required libraries to create an api
from flask import Flask, jsonify, request
from hp_model import house_price 

app = Flask(__name__)

@app.route("/pred", methods = ["POST"]) # routing api to 127.0.0.1/pred and using POST method
def predictions():
    try:
        data = request.get_json() # storing data in variable that posted through api
        area = data["area"]
        rooms = data["rooms"]
        floors = data["floors"]
        garage = data["garage"]
        price = house_price.model(area, rooms, floors, garage) # using pre-trained model for prediction

        return jsonify({"Price of the House: ": price })

    except:
        return jsonify({"Error": "Please check given input"})

app.run(debug=True, port=8080)