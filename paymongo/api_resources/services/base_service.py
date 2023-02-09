import paymongo
from paymongo import ApiResource
from paymongo import ListingEntity
from paymongo import PaymongoConfig
from paymongo import PaymongoClient
from paymongo import StandardException

class BaseService():
  def __init__(self) -> None:
    pass

  def config():
    return PaymongoConfig(paymongo.api_key)

  def request(method, entity, path, payload={}, is_listing=False):
    api_resource = PaymongoClient.execute_request(
      config=BaseService.config(),
      method=method,
      params=payload,
      path=path
    )

    if is_listing:
      data = list(map(lambda data: entity(ApiResource(response=data)), api_resource.data))
      return ListingEntity(data=data, has_more=api_resource.has_more)

    return entity(api_resource=api_resource)
