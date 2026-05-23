import os
import requests
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import json

load_dotenv()

app = FastAPI(title="News Digest API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OLLAMA_URL   = "http://localhost:11434/api/generate"
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")


@app.get("/")
def root():
    return FileResponse("index.html")


@app.get("/api/news")
def fetch_news(topic: str = "technology", count: int = Query(5, ge=1, le=20)):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q":        topic,
        "pageSize": count,
        "language": "en",
        "sortBy":   "publishedAt",
        "apiKey":   NEWS_API_KEY,
    }
    res = requests.get(url, params=params)
    data = res.json()

    if data.get("status") != "ok":
        return {"error": data.get("message", "Unknown error"), "articles": []}

    articles = [
        {
            "title":       a.get("title") or "No title",
            "description": a.get("description") or "",
            "source":      (a.get("source") or {}).get("name") or "Unknown",
            "url":         a.get("url") or "",
            "publishedAt": a.get("publishedAt") or "",
            "urlToImage":  a.get("urlToImage") or "",
        }
        for a in data.get("articles", [])
        if "[Removed]" not in (a.get("title") or "")
    ]
    return {"articles": articles, "total": len(articles)}


@app.get("/api/summarize")
def summarize_stream(title: str, description: str = ""):
    prompt = f"""Summarize this news in 2 short sentences. Be direct, no filler words.

Title: {title}
Description: {description or 'Not available'}

Summary:"""

    def generate():
        try:
            res = requests.post(
                OLLAMA_URL,
                json={"model": OLLAMA_MODEL, "prompt": prompt, "stream": True},
                stream=True,
                timeout=60,
            )
            res.raise_for_status()
            for line in res.iter_lines():
                if line:
                    chunk = json.loads(line)
                    token = chunk.get("response", "")
                    if token:
                        yield token
                    if chunk.get("done"):
                        break
        except requests.exceptions.ConnectionError:
            yield "⚠ Ollama not running — start it with: ollama serve"
        except Exception as e:
            yield f"⚠ Summarization failed: {e}"

    return StreamingResponse(generate(), media_type="text/plain")


@app.get("/api/health")
def health():
    """Check if Ollama is reachable."""
    try:
        r = requests.get("http://localhost:11434", timeout=3)
        return {"ollama": "ok"}
    except Exception:
        return {"ollama": "offline"}