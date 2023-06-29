from paymongo import BaseEntity
from paymongo import BillingEntity
from paymongo import LineItemEntity
from paymongo.api_resources.api_resource import ApiResource
from paymongo import PaymentEntity
from paymongo import PaymentIntentEntity

class CheckoutSessionEntity(BaseEntity):
  def __init__(self, api_resource):
    BaseEntity.__init__(self)

    self.id = api_resource.id
    self.type = api_resource.type
    self.billing = BillingEntity(api_resource.attributes['billing'])
    self.cancel_url = api_resource.attributes['cancel_url']
    self.checkout_url = api_resource.attributes['checkout_url']
    self.client_key = api_resource.attributes['client_key']
    self.description = api_resource.attributes['description']
    self.line_items = []

    if (api_resource.attributes['line_items'] and
          isinstance(api_resource.attributes['line_items'], list)):
      line_items = api_resource.attributes['line_items']

      for line_item in line_items:
        rowApiResource = ApiResource(line_item)
        self.line_items.append(LineItemEntity(rowApiResource))

    self.livemode = api_resource.attributes['livemode']
    self.merchant = api_resource.attributes['merchant']

    if (api_resource.attributes['payments'] and
          isinstance(api_resource.attributes['payments'], list)):
      payments = api_resource.attributes['payments']

      for payment in payments:
        rowApiResource = ApiResource(payment)
        self.payments.append(PaymentEntity(rowApiResource))

    self.payment_intent = PaymentIntentEntity(api_resource.attributes['payment_intent'])
    self.payment_method_types = api_resource.attributes['payment_method_types']
    self.reference_number = api_resource.attributes['reference_number']
    self.send_email_receipt = api_resource.attributes['send_email_receipt']
    self.show_description = api_resource.attributes['show_description']
    self.show_line_items = api_resource.attributes['show_line_items']
    self.status = api_resource.attributes['status']
    self.success_url = api_resource.attributes['success_url']
    self.created_at = api_resource.attributes['created_at']
    self.updated_at = api_resource.attributes['updated_at']
    self.metadata = api_resource.attributes['metadata']
