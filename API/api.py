from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def get_data():
	if request.method == "GET":
		data = json.load(open("./signals.json"))
		print(data)
		return jsonify(data)


@app.route("/search", methods=["GET"])
def search():
	args = request.args
	name = args.get("name") 
	if request.method == "GET":
		data = json.load(open("./signals.json"))
		if args:
			for r in data:
				if r["name"].lower() == name.lower():
					return jsonify(r)
			return jsonify({"error": "No results found"})
		return jsonify({"error": "No search parameters provided"})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=4000, debug=True)
