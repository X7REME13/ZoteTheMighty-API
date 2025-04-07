import random
from typing import Union

from fastapi import FastAPI

import json

app = FastAPI()

precepts_es = []
precepts_en = []

cant_of_precepts = 57


with open("data/precepts.en.json", "r", encoding="utf-8") as file:
    precepts_en = json.load(file)

with open("data/precepts.es.json", "r", encoding="utf-8") as file:
    precepts_es = json.load(file)

if not precepts_en or not precepts_es:
    raise RuntimeError("No se pudieron cargar los preceptos.")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/precept")
def get_random_precept(lang: str = "en"):
    if lang == "es":
        return random.choice(precepts_es)
    elif lang == "en":
        return random.choice(precepts_en)
    else:
        return {"error": "Idioma no soportado. Usa 'en' o 'es'."}
