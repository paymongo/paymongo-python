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