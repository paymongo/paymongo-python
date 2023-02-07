from paymongo import BaseEntity

class RefundEntity(BaseEntity):
  def __init__(self, resource):
    BaseEntity.__init__(self)

    data = resource['data']
    attributes = data['attributes']

    self.id = data['id']
    self.amount = attributes['amount']
    self.balance_transaction_id = attributes['balance_transaction_id']
    self.currency = attributes['currency']
    self.livemode = attributes['livemode']
    self.metadata = attributes['metadata']
    self.notes = attributes['notes']
    self.payment_id = attributes['payment_id']
    self.payout_id = attributes['payout_id']
    self.reason = attributes['reason']
    self.status = attributes['status']
    self.available_at = attributes['available_at']
    self.created_at = attributes['created_at']
    self.refunded_at = attributes['refunded_at']
    self.updated_at = attributes['updated_at']
