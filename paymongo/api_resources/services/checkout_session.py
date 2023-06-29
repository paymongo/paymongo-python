from paymongo import BaseService
from paymongo import CheckoutSessionEntity

class CheckoutSession(BaseService):
  URI = 'checkout_sessions'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def create(self, payload):
    return self.request(
      entity=CheckoutSessionEntity,
      method='post',
      path=f'{self.URI}',
      payload=payload
    )

  @classmethod
  def retrieve(self,id):
    return self.request(
      entity=CheckoutSessionEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )

  @classmethod
  def expire(self,id):
    return self.request(
      entity=CheckoutSessionEntity,
      method='post',
      path=f'{self.URI}/{id}/expire'
    )