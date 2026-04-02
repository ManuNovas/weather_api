from http.client import HTTPException
from json import dumps

from aws_lambda_powertools import Logger

from src.application.ports.input import WeatherInputPort


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
        except HTTPException as e:
            self.logger.error(e)
            code, message = e.args
            response = {
                "statusCode": code if code else 500,
                "body": message if message else "Internal Server Error",
            }
        return response
