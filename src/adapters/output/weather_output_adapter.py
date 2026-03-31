from requests import get

from src.application.ports.output import WeatherOutputPort


class WeatherOutputAdapter(WeatherOutputPort):
    def get_timeline(self, location: str) -> dict:
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}"
        response = get(url)
        return response.json()
