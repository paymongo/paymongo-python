import paymongo
from paymongo import PaymongoConfig
from paymongo import PaymongoClient
from paymongo import PaymentIntentEntity
from paymongo import StandardException

class BaseService(object):
  def __init__(self) -> None:
    pass

  def config():
    if paymongo.api_key == None:
      raise StandardException('API key is required.')

    return PaymongoConfig(paymongo.api_key)

  def request(method, object, path, payload={}):
    response = PaymongoClient.execute_request(
      config=BaseService.config(),
      method=method,
      params=payload,
      path=path
    )

    return BaseService.toEntity(object, response)

  def toEntity(object, response):
    entities = {
      'payment_intent_entity' : PaymentIntentEntity(resource=response)
    }

    return entities[object]
