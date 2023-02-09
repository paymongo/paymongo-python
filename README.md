# paymongo-python

# PayMongo Python Library

PayMongo python library provides python applications an easy access to the PayMongo API. Explore various classes that can represent API resources on object instantiation. The goal of this library is simplify PayMongo integration with any python application.

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

# set api key config
paymongo.api_key='sk_test...'

# retrieve payment intent
paymongo.PaymentIntent.retrieve('pi_...')

# create payment intent
payment_intent = paymongo.PaymentIntent.create({
  'amount': 10000,
  'currency': 'PHP',
  'description': 'Dog Treat',
  'payment_method_allowed': [
    'card'
  ],
  'statement_descriptor': 'BarkerShop',
  'currency': 'PHP'
})

# retrieve payment intent id attribute
payment_intent.id
 => "pi_..."

# retrieve payment intent status attribute
payment_intent.status
 => "awaiting_payment_method"

# retrieve payment method
paymongo.PaymentMethod.retrieve('pm_...')

# create payment method
paymongo.PaymentMethod.create({
  'type': 'card',
  'details': {
    'card_number': '5111111111111118',
    'exp_month': 3,
    'exp_year': 2025,
    'cvc': '123'
  },
  'billing': {
    'address': {
      'line1': 'test line2',
      'line2': 'test line 1',
      'city': 'Antipolo',
      'state': 'Rizal',
      'postal_code': '1870',
      'country': 'PH'
    },
    'email': 'juan@gmail.comm',
    'name': 'Juan dela cruz',
    'phone': '09176318683'
  }
})

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
  'metadata': {
    '1': '1'
  },
  'phone': '+639150000001'
})

paymongo.Customer.update('cus_...', {
  'default_device': 'phone',
  'email': 'test2@paymongo.com',
  'first_name': 'Pay',
  'last_name': 'Mongo',
  'phone': '+639150000002'
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
