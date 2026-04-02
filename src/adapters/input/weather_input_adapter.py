from json import dumps

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.validation import validator

from src.application.ports.input import WeatherInputPort
from src.adapters.input.schemas import LOCATION_SCHEMA


class WeatherInputAdapter:
    input_port: WeatherInputPort
    logger: Logger

    def __init__(self, input_port: WeatherInputPort):
        self.input_port = input_port
        self.logger = Logger(service="WeatherInputAdapter")

    def handler(self, event):
        try:
            timeline = self.input_port.get_timeline(event["pathParameters"]["location"])
            response = {
                "statusCode": 200,
                "body": dumps(timeline),
            }
        except Exception as e:
            self.logger.error(e)
            response = {
                "statusCode": 500,
                "body": dumps({"error": "Internal Server Error"}),
            }
        return response
