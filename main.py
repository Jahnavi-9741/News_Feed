# main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "5a75424100fb434ea4637e6b1a4e1aa2"  # ← get one from https://newsapi.org/

@app.get("/search")
def search_news(q: str = Query(...)):
    url = f"https://newsapi.org/v2/everything?q={q}&apiKey={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return {"articles": [], "error": "Failed to fetch news"}
