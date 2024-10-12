#!/usr/bin/python3
"""python"""
from flask import Flask, jsonify, request


app = Flask(__name__)
users = {"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
         "rahman": {"username": "rahman", "name": "Rahman", "age": 18, "city": "Baku"},
         "fidan": {"username": "fidan", "name": "Fidan", "age": 28, "city": "Ganja"}}
@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    user = list(users)
    return jsonify(user)

@app.post("/add_user")
def add():
    data = request.json
    user = {
        "username": data.get("username"),
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    if user["username"] is None:
        return {"error":"Username is required"}, 400
    users[data.get("username")] = user
    return f"user added", 201


@app.route("/users/<username>")
def user(username):
    if users.get(username) is None:
        return {"error": "User not found"}
    return jsonify(users.get(username)), 200

@app.route("/status")
def status():
    return "OK"

if __name__ == "__main__":
    app.run(debug=True)
