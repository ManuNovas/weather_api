from unittest import TestCase

from src.adapters.output import WeatherOutputAdapter


class TestWeatherOutputAdapter(TestCase):
    adapter: WeatherOutputAdapter

    def setUp(self):
        self.adapter = WeatherOutputAdapter()

    def test_get_timeline(self):
        result = self.adapter.get_timeline("Tlalpan")
        self.assertIsNotNone(result)
