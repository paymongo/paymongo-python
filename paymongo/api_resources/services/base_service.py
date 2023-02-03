import paymongo
from paymongo import PaymongoConfig
from paymongo import PaymongoClient
from paymongo import StandardException

class BaseService():
  def __init__(self) -> None:
    pass

  def config():
    if paymongo.api_key == None:
      raise StandardException('API key is required.')

    return PaymongoConfig(paymongo.api_key)

  def request(method, entity, path, payload={}):
    response = PaymongoClient.execute_request(
      config=BaseService.config(),
      method=method,
      params=payload,
      path=path
    )

    return entity(resource=response)
