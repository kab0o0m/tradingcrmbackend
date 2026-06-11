from fastapi import APIRouter
import requests

router = APIRouter()

API_KEY = "d8le0l9r01qtamgu9u6gd8le0l9r01qtamgu9u70"

@router.get("/news")
def get_news():

    url = (
        "https://finnhub.io/api/v1/news"
    )

    params = {
        "category": "forex",
        "token": API_KEY
    }

    response = requests.get(
        url,
        params=params
    )

    if response.status_code == 200:
        return response.json()

    return {
        "error":
        "Failed to fetch news"
    }