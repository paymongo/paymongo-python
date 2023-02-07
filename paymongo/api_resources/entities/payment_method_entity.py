from paymongo import BaseEntity

class PaymentMethodEntity(BaseEntity):
  def __init__(self, resource):
    BaseEntity.__init__(self)

    data = resource['data']
    attributes = data['attributes']

    self.id = data['id']
    self.billing = attributes['billing']
    self.details = attributes['details']
    self.livemode = attributes['livemode']
    self.metadata = attributes['metadata']
    self.type = attributes['type']
    self.created_at = attributes['created_at']
    self.updated_at = attributes['updated_at']
