from dotenv import load_dotenv
from functools import lru_cache
from os import getenv
from requests import get

from src.application.ports.output import WeatherOutputPort

load_dotenv()


class WeatherOutputAdapter(WeatherOutputPort):
    @lru_cache(maxsize=128)
    def get_timeline(self, location: str) -> dict:
        key = getenv("VISUAL_CROSSING_KEY")
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?key={key}"
        response = get(url)
        if response.status_code != 200:
            raise Exception(code=response.status_code, message=response.text)
        return response.json()
