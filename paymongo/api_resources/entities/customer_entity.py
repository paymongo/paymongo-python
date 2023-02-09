from paymongo import BaseEntity

class CustomerEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    attributes = api_resource.attributes

    self.id = api_resource.id
    self.default_device = self.get_value(attributes, 'default_device')
    self.default_payment_method_id = self.get_value(attributes, 'default_payment_method_id')
    self.deleted = self.get_value(attributes, 'deleted')
    self.email = self.get_value(attributes, 'email')
    self.first_name = self.get_value(attributes, 'first_name')
    self.last_name = self.get_value(attributes, 'last_name')
    self.livemode = self.get_value(attributes, 'livemode')
    self.phone = self.get_value(attributes, 'phone')
    self.type = self.get_value(attributes, 'type')
    self.created_at = self.get_value(attributes, 'created_at')
    self.updated_at = self.get_value(attributes, 'updated_at')
