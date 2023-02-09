from paymongo import BaseEntity

class BillingAddressEntity(BaseEntity):
  def __init__(self, data):
    BaseEntity.__init__(self)

    self.city = data['city']
    self.country = data['country']
    self.line1 = data['line1']
    self.line2 = data['line2']
    self.postal_code = data['postal_code']
    self.state = data['state']
