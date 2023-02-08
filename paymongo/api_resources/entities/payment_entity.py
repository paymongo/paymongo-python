from paymongo import BaseEntity

class PaymentEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.access_url = api_resource.attributes['access_url']
    self.amount = api_resource.attributes['amount']
    self.balance_transaction_id = api_resource.attributes['balance_transaction_id']
    self.billing = api_resource.attributes['billing']
    self.currency = api_resource.attributes['currency']
    self.description = api_resource.attributes['description']
    self.disputed = api_resource.attributes['disputed']
    self.external_reference_number = api_resource.attributes['external_reference_number']
    self.fee = api_resource.attributes['fee']
    self.foreign_fee = api_resource.attributes['foreign_fee'] if 'foreign_fee' in api_resource.attributes else None
    self.livemode = api_resource.attributes['livemode']
    self.metadata = api_resource.attributes['metadata']
    self.net_amount = api_resource.attributes['net_amount']
    self.origin = api_resource.attributes['origin']
    self.payment_intent_id = api_resource.attributes['payment_intent_id']
    self.payout = api_resource.attributes['payout']
    self.refunds = api_resource.attributes['refunds']
    self.source = api_resource.attributes['source']
    self.statement_descriptor = api_resource.attributes['statement_descriptor']
    self.status = api_resource.attributes['status']
    self.tax_amount = api_resource.attributes['tax_amount']
    self.taxes = api_resource.attributes['taxes']
    self.available_at = api_resource.attributes['available_at'] if 'available_at' in api_resource.attributes else None
    self.created_at = api_resource.attributes['created_at']
    self.paid_at = api_resource.attributes['paid_at']
    self.updated_at = api_resource.attributes['updated_at']
