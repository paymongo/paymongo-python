from paymongo import BaseEntity

class EventEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.resource = api_resource.attributes['resource']
    self.type = api_resource.attributes['type']
