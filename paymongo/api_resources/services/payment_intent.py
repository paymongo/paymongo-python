from paymongo import BaseService

class PaymentIntent(BaseService):
  URI = 'payment_intents'

  def __init__(self, config):
    BaseService.__init__(self, config=config)

  def create(self, payload):
    return self.request(
      method='post',
      object='payment_intent_entity',
      path=self.URI,
      payload=payload
    )

  def retrieve(self, id):
    return self.request(
      method='get',
      object='payment_intent_entity',
      path=f'{self.URI}/{id}'
    )
