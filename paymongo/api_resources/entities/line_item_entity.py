from paymongo import BaseEntity

class LineItemEntity(BaseEntity):
  def __init__(self, data):
    BaseEntity.__init__(self)

    self.amount = data['amount']
    self.currency = data['currency']
    self.description = data['description']
    self.images = data['images']
    self.name = data['name']
    self.quantity = data['quantity']
