from paymongo import BaseEntity

class PaymentEntity(BaseEntity):
  def __init__(self, resource):
    BaseEntity.__init__(self)

    data = resource['data']
    attributes = data['attributes']

    self.id = data['id']
    self.access_url = attributes['access_url']
    self.amount = attributes['amount']
    self.balance_transaction_id = attributes['balance_transaction_id']
    self.billing = attributes['billing']
    self.currency = attributes['currency']
    self.description = attributes['description']
    self.disputed = attributes['disputed']
    self.external_reference_number = attributes['external_reference_number']
    self.fee = attributes['fee']
    self.foreign_fee = attributes['foreign_fee'] if 'foreign_fee' in attributes else None
    self.livemode = attributes['livemode']
    self.metadata = attributes['metadata']
    self.net_amount = attributes['net_amount']
    self.origin = attributes['origin']
    self.payment_intent_id = attributes['payment_intent_id']
    self.payout = attributes['payout']
    self.refunds = attributes['refunds']
    self.source = attributes['source']
    self.statement_descriptor = attributes['statement_descriptor']
    self.status = attributes['status']
    self.tax_amount = attributes['tax_amount']
    self.taxes = attributes['taxes']
    self.available_at = attributes['available_at']
    self.created_at = attributes['created_at']
    self.paid_at = attributes['paid_at']
    self.updated_at = attributes['updated_at']
