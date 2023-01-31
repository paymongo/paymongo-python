from paymongo import PaymongoClient
from paymongo import PaymentIntentEntity

class BaseService(object):
  def __init__(self, config):
    self.config = config

  def request(self, method, object, path, payload={}):
    response = PaymongoClient.execute_request(
      config=self.config,
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
