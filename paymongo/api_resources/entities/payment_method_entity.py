from paymongo import BaseEntity

class PaymentMethodEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.billing = api_resource.attributes['billing']
    self.details = api_resource.attributes['details']
    self.livemode = api_resource.attributes['livemode']
    self.metadata = api_resource.attributes['metadata']
    self.type = api_resource.attributes['type']
    self.created_at = api_resource.attributes['created_at']
    self.updated_at = api_resource.attributes['updated_at']
