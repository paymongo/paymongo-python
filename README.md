# PayMongo Python Library

PayMongo Python library provides python applications an easy access to the PayMongo API. Explore various classes that can represent API resources on object instantiation. The goal of this library is simplify PayMongo integration with any python application.

## Pending TODOs

- TBD

## Documentation

See the [PayMongo API docs](https://developers.paymongo.com/reference/getting-started-with-your-api).

### Requirements

- Python 3.9.+

## Installation

You don't need this source code unless you want to modify the library. If you just
want to use the package, just run:

```sh
pip3 install paymongo-python
```

If you want to run the library from source:

Create a virtual environment

```sh
python3 -m venv env
```

Activate the virtual environment

```sh
source env/bin/activate
```

Installing package to virtual environment (editable)

```sh
pip3 install -e paymongo-python

python
```

## Usage

The library needs to be configured with your account's secret key which is
available in your [PayMongo Dashboard][api-keys]. Initialize the library to its
value:

```python
import paymongo

# Set api key config
paymongo.api_key='sk_test...'

# Payment Method
payment_method = paymongo.PaymentMethod.retrieve('pm_...')

# Retrieve attributes
payment_method.id
 => "pm_..."

payment_method.type
 => "card"

paymongo.PaymentMethod.create({
  'type': 'card',
  'details': {
    'card_number': '5111111111111118',
    'cvc': '123',
    'exp_month': 3,
    'exp_year': 2025,
  },
  'billing': {
    'address': {
      'line1': 'test line 1',
      'line2': 'test line 2',
      'city': 'Antipolo',
      'state': 'Rizal',
      'postal_code': '1870',
      'country': 'PH'
    },
    'email': 'test@paymongo.com',
    'name': 'Pay Mongo',
    'phone': '09123456789'
  }
})

# Payment Intent
paymongo.PaymentIntent.retrieve('pi_...')

payment_intent = paymongo.PaymentIntent.create({
  'amount': 10000,
  'currency': 'PHP',
  'description': 'Dog Treat',
  'payment_method_allowed': [
    'card'
  ],
  'statement_descriptor': 'BarkerShop'
})

paymongo.PaymentIntent.attach('pi_...', {
  'payment_method': 'pm_...',
  'return_url': 'https://test/success'
})

paymongo.PaymentIntent.cancel('pi_...')

paymongo.PaymentIntent.capture('pi_...', {
  'amount':10000
})

# Payment
paymongo.Payment.retrieve('pay_...')

# Refund
paymongo.Refund.retrieve('ref_...')

paymongo.Refund.create({
  'amount': 10000,
  'payment_id': 'pay_...',
  'reason': 'requested_by_customer',
  'metadata': {
    'merchant': 'test value'
  }
})
```

## Customers

```python
paymongo.Customer.retrieve('cus_...')

paymongo.Customer.create({
  'default_device': 'phone',
  'email': 'test@paymongo.com',
  'first_name': 'Pay',
  'last_name': 'Mongo',
  'phone': '+624123456789'
})

paymongo.Customer.update('cus_...', {
  'default_device': 'phone',
  'email': 'test@paymongo.com',
  'first_name': 'Pay',
  'last_name': 'Mongo',
  'phone': '+649223456789'
})

paymongo.Customer.delete('cus_...')
```

## Links

```python
paymongo.Link.retrieve('link_...')

paymongo.Link.archive('link_...')

paymongo.Link.unarchive('link_...')

paymongo.Link.create({
  'amount': 10000,
  'description': 'link description',
  'remarks': 'link remarks'
})

links = paymongo.Link.all({'reference_number': '1234abc'})
```

## Webhooks

```python
paymongo.Webhook.retrieve('hook_...')

paymongo.Webhook.create({
  'events': ['payment.refunded', 'payment.refund.updated'],
  'url': 'http://localhost:3100/webhook'
})

paymongo.Webhook.disable('hook_...')

paymongo.Webhook.enable('hook_...')

paymongo.Webhook.update('hook_...', {
   'events': ['payment.refunded', 'payment.refund.updated'],
   'url': 'http://localhost:3001/webhook'
})

webhooks = paymongo.Webhook.all()
```

## Handle errors

```python
try:
  payment_intent = paymongo.PaymentIntent.retrieve('pi_...')
except paymongo.StandardException as e:
  # Handle error
  print(e.errors[0].detail)
  print(e.errors[0].code)
```

## Verifying webhook signature

```python
payload = '{"data":{"id":"evt_...","type":"event","attributes":{"type":"source.chargeable"},"created_at":1675323264}}}'
signature_header = 't=1675323267,te=,li=99f...'
webhook_secret_key = 'whsk_...'

try:
  event = paymongo.Webhook.construct_event(
    payload=payload,
    signature_header=signature_header,
    webhook_secret_key=webhook_secret_key
  )

  event.id
  event.type
  event.resource
except paymongo.SignatureVerificationException:
  # Handle invalid signature
```
