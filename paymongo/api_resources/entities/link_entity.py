from paymongo import BaseEntity

class LinkEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.amount = api_resource.attributes['amount']
    self.archived = api_resource.attributes['archived']
    self.checkout_url = api_resource.attributes['checkout_url']
    self.currency = api_resource.attributes['currency']
    self.description = api_resource.attributes['description']
    self.fee = api_resource.attributes['fee']
    self.livemode = api_resource.attributes['livemode']
    self.payments = api_resource.attributes['payments']
    self.reference_number = api_resource.attributes['reference_number']
    self.remarks = api_resource.attributes['remarks']
    self.status = api_resource.attributes['status']
    self.tax_amount = api_resource.attributes['tax_amount']
    self.taxes = api_resource.attributes['taxes']
    self.created_at = api_resource.attributes['created_at']
    self.updated_at = api_resource.attributes['updated_at']
