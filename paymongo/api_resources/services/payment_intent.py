from paymongo import BaseService
from paymongo import PaymentIntentEntity;

class PaymentIntent(BaseService):
  URI = 'payment_intents'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def attach(self, id, payload):
    return self.request(
      entity=PaymentIntentEntity,
      method='post',
      path=f'{self.URI}/{id}/attach',
      payload=payload
    )

  @classmethod
  def cancel(self, id):
    return self.request(
      entity=PaymentIntentEntity,
      method='post',
      path=f'{self.URI}/{id}/cancel'
    )

  @classmethod
  def capture(self, id, payload):
    return self.request(
      entity=PaymentIntentEntity,
      method='post',
      path=f'{self.URI}/{id}/capture',
      payload=payload
    )

  @classmethod
  def create(self, payload):
    return self.request(
      entity=PaymentIntentEntity,
      method='post',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=PaymentIntentEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )
