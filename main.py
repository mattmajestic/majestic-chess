from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
import requests
import httpx

app = FastAPI()

@app.get("/")
def read_root():
    response = RedirectResponse(url='/docs')
    return response

@app.get("/profile/{username}")
async def read_item(username: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f'https://api.chess.com/pub/player/{username}')
        if response.status_code == 200:
            try:
                data = response.json()
                return data
            except ValueError:
                return {"error": "Unable to decode JSON", "response": response.text}
        else:
            return {"error": "Unable to fetch profile"}