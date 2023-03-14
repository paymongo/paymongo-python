import hashlib
import hmac
import json

from paymongo import ApiResource
from paymongo import BaseService
from paymongo import EventEntity
from paymongo import SignatureVerificationException
from paymongo import UnexpectedValueException
from paymongo import WebhookEntity

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
  def construct_event(all, payload, signature_header, webhook_secret_key):
    if not type(signature_header) == str:
      raise UnexpectedValueException('The signature must be a string.')

    signature_array = signature_header.split(',')

    if len(signature_array) < 3:
      raise UnexpectedValueException(f'The format of signature {signature_header} is invalid.')

    timestamp = signature_array[0].split('=')[1]
    test_mode_signature = signature_array[1].split('=')[1]
    live_mode_signature = signature_array[2].split('=')[1]

    if test_mode_signature is not None:
      comparison_signature = test_mode_signature

    if live_mode_signature is not None:
      comparison_signature = live_mode_signature

    hash = hmac.new(
      bytes(webhook_secret_key, 'utf-8'),
      bytes(f'{timestamp}.{payload}', 'utf-8'),
      hashlib.sha256
    ).hexdigest()

    if hash != comparison_signature:
      raise SignatureVerificationException('The signature is invalid.')

    api_source = ApiResource(response=json.loads(payload))

    return EventEntity(api_resource=api_source)

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
