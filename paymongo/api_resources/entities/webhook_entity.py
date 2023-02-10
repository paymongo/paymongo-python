from paymongo import BaseEntity

class WebhookEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.events = api_resource.attributes['events']
    self.livemode = api_resource.attributes['livemode']
    self.secret_key = api_resource.attributes['secret_key']
    self.status = api_resource.attributes['status']
    self.url = api_resource.attributes['url']
    self.created_at = api_resource.attributes['created_at']
    self.updated_at = api_resource.attributes['updated_at']
