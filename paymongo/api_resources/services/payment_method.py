from paymongo import BaseService
from paymongo import PaymentMethodEntity;

class PaymentMethod(BaseService):
  URI = 'payment_methods'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def create(self, payload):
    return self.request(
      entity=PaymentMethodEntity,
      method='post',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=PaymentMethodEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )
