import rollbar
from rollbar.handler import RollbarNotifier

rollbar.init(
  access_token='d3083ebee2574328bba7d597f5797041',
  environment='testenv',
  code_version='1.0'
)


logger = rollbar.get_current_logger()
