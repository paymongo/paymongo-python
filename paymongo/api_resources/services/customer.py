from paymongo import BaseService
from paymongo import CustomerEntity;

class Customer(BaseService):
  URI = 'customers'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def create(self, payload):
    return self.request(
      entity=CustomerEntity,
      method='post',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def delete(self, id):
    return self.request(
      entity=CustomerEntity,
      method='delete',
      path=f'{self.URI}/{id}'
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=CustomerEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )

  @classmethod
  def update(self, id, payload):
    return self.request(
      entity=CustomerEntity,
      method='put',
      path=f'{self.URI}/{id}',
      payload=payload
    )
