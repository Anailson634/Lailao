from flask import Flask, request, jsonify
from flask_cors import CORS
from gerar_carros import gerar_lista
import json


app=Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def post_carro():
    db_carro=None
    with open("python/meus_carros.json", 'r', encoding="utf8") as arq:
        db_carro=json.load(arq)
    return db_carro

@app.route("/gerar_carros", methods=["POST"])
def gerar_carros():
    response_get=request.json

    carros=gerar_lista(response_get['quantidade'])
    return jsonify(carros), 200

if __name__=="__main__":
    app.run()
    