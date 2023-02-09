from paymongo import BaseService
from paymongo import WebhookEntity;

class Webhook(BaseService):
  URI = 'webhooks'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def all(self):
    return self.request(
      entity=WebhookEntity,
      method='get',
      path=self.URI,
      is_listing=True
    )

  @classmethod
  def create(self, payload):
    return self.request(
      entity=WebhookEntity,
      method='post',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def disable(self, id):
    return self.request(
      entity=WebhookEntity,
      method='post',
      path=f'{self.URI}/{id}/disable'
    )

  @classmethod
  def enable(self, id):
    return self.request(
      entity=WebhookEntity,
      method='post',
      path=f'{self.URI}/{id}/enable'
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=WebhookEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )

  @classmethod
  def update(self, id, payload):
    return self.request(
      entity=WebhookEntity,
      method='put',
      path=f'{self.URI}/{id}',
      payload=payload
    )
