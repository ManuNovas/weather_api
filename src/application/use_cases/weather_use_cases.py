from src.application.ports.input import WeatherInputPort
from src.application.ports.output import WeatherOutputPort


class WeatherUseCases(WeatherInputPort):
    output_port: WeatherOutputPort

    def __init__(self, output_port: WeatherOutputPort):
        self.output_port = output_port

    def get_timeline(self, location: str) -> dict:
        return self.output_port.get_timeline(location)
