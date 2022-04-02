from fastapi import FastAPI, Query
import json

app = FastAPI()

@app.get("/")

def get_current_ouput():
	with open('./signals.json', 'r') as file:
		return json.load(file)

# @app.get("/get_by_pair/{pair}")

# def get_single_pair(pair: str):
	
# 	return