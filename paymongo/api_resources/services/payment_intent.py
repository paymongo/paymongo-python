from paymongo import BaseService

class PaymentIntent(BaseService):
  URI = 'payment_intents'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def create(self, payload):
    return self.request(
      method='post',
      object='payment_intent_entity',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      method='get',
      object='payment_intent_entity',
      path=f'{self.URI}/{id}'
    )
