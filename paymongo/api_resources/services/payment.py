from paymongo import BaseService
from paymongo import PaymentEntity;

class Payment(BaseService):
  URI = 'payments'

  def __init__(self):
    BaseService.__init__(self)

  @classmethod
  def retrieve(self, id):
    return self.request(
      entity=PaymentEntity,
      method='get',
      path=f'{self.URI}/{id}'
    )
