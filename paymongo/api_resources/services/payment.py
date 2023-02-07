from paymongo import BaseService
from paymongo import PaymentEntity;

class Payment(BaseService):
  URI = 'payments'

  def __init__(self, config):
    BaseService.__init__(self, config=config)

  @classmethod
  def retrieve(self, id):
    return self.request(
      method='get',
      entity=PaymentEntity,
      path=f'{self.URI}/{id}'
    )
