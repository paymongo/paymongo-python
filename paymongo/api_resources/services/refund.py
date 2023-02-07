from paymongo import BaseService
from paymongo import RefundEntity;

class Refund(BaseService):
  URI = 'refunds'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def create(self, payload):
    return self.request(
      entity=RefundEntity,
      method='post',
      path=self.URI,
      payload=payload
    )

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=RefundEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )
