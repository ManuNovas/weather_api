from abc import ABC, abstractmethod


class WeatherInputPort(ABC):
    @abstractmethod
    def get_timeline(self, location: str) -> dict:
        pass
