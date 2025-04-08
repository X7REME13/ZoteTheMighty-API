from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import json
import random

app = FastAPI(
    title="Zote, The Mighty - API",
    description="A simple API to learn the 'Fifty-Seven Precepts of Zote'.",
    version="1.0.0"
)

# ----- CLASES ----- #

class Precept(BaseModel):
    number: int
    title: str
    description: str
    

# ----- DATA LOAD ----- #

precepts_es = []
precepts_en = []

with open("data/precepts.en.json", "r", encoding="utf-8") as file:
    precepts_en = json.load(file)

with open("data/precepts.es.json", "r", encoding="utf-8") as file:
    precepts_es = json.load(file)

if not precepts_en or not precepts_es:
    raise RuntimeError("Failed to load precepts from JSON files. Please check the files.")

# ----- ENDPOINTS ----- #

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/precept")
def get_random_precept(lang: str = "en"):
    """
    Endpoint to retrieve a random precept.
    """
    if lang == "es":
        return random.choice(precepts_es)
    elif lang == "en":
        return random.choice(precepts_en)
    else:
        return {"error": "Invalid language. Use 'en' or 'es'."}
    
    
@app.get("/precept/{id}")
def get_precept_by_index(id: int, lang: str = "en") -> Union[Precept, dict]:
    """
    Endpoint to retrieve a precept by number.
    """
    data = precepts_en if lang == "en" else precepts_es

    if 0 < id <= len(data):
        return data[id - 1]
    else:
        return {"error": "Id out of range."}


