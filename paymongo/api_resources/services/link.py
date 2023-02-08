from paymongo import BaseService
from paymongo import LinkEntity;

class Link(BaseService):
  URI = 'links'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def all(self, payload):
    return self.request(
      entity=LinkEntity,
      method='get',
      path=self.URI,
      payload=payload,
      is_listing=True
    )

  @classmethod
  def archive(self, id):
    return self.request(
      entity=LinkEntity,
      method='post',
      path=f'{self.URI}/{id}/archive'
    )

  @classmethod
  def create(self, payload):
    return self.request(
      entity=LinkEntity,
      method='post',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=LinkEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )

  @classmethod
  def unarchive(self, id):
    return self.request(
      entity=LinkEntity,
      method='post',
      path=f'{self.URI}/{id}/unarchive'
    )
