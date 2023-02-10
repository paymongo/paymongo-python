from paymongo import BaseEntity
from paymongo import BillingAddressEntity

class BillingEntity(BaseEntity):
  def __init__(self, data):
    BaseEntity.__init__(self)

    self.address = BillingAddressEntity(data['address'])
    self.email = data['email']
    self.name = data['name']
    self.phone = data['phone']
