from abc import ABC, abstractmethod


class WeatherOutputPort(ABC):
    @abstractmethod
    def get_timeline(self, location: str) -> dict:
        pass
