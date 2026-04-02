from aws_lambda_powertools.utilities.validation import validator

from src.adapters.input import WeatherInputAdapter
from src.adapters.input.schemas import LOCATION_SCHEMA
from src.adapters.output import WeatherOutputAdapter
from src.application.use_cases import WeatherUseCases


@validator(inbound_schema=LOCATION_SCHEMA)
def handler(event, context):
    output_adapter = WeatherOutputAdapter()
    use_cases = WeatherUseCases(output_adapter)
    input_adapter = WeatherInputAdapter(use_cases)
    return input_adapter.handler(event)
