from paymongo import BaseEntity

class RefundEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.amount = api_resource.attributes['amount']
    self.balance_transaction_id = api_resource.attributes['balance_transaction_id']
    self.currency = api_resource.attributes['currency']
    self.livemode = api_resource.attributes['livemode']
    self.metadata = api_resource.attributes['metadata']
    self.notes = api_resource.attributes['notes']
    self.payment_id = api_resource.attributes['payment_id']
    self.payout_id = api_resource.attributes['payout_id']
    self.reason = api_resource.attributes['reason']
    self.status = api_resource.attributes['status']
    self.available_at = api_resource.attributes['available_at']
    self.created_at = api_resource.attributes['created_at']
    self.refunded_at = api_resource.attributes['refunded_at']
    self.updated_at = api_resource.attributes['updated_at']
