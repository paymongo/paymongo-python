from paymongo.api_resources.exceptions.standard_exception import StandardException

from paymongo.api_resources.paymongo_config import PaymongoConfig
from paymongo.api_resources.paymongo_client import PaymongoClient

from paymongo.api_resources.entities.base_entity import BaseEntity
from paymongo.api_resources.entities.payment_intent_entity import PaymentIntentEntity

from paymongo.api_resources.services.base_service import BaseService
from paymongo.api_resources.services.payment_intent import PaymentIntent

api_key = None

def payment_intent():
  if api_key == None:
    raise StandardException('API key is required.')

  return PaymentIntent(config=PaymongoConfig(api_key))
