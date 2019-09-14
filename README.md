# Paymongo Python SDK

## Usage
The library needs to be configured with your account's secret key which is available in your [Paymongo Dashboard](https://dashboard.paymongo.com/developers). Set paymongo.api_key to its value:
```python
import paymongo
paymongo.api_key = 'sk_test_...'

# create payment
payment = paymongo.Payment.create({
'amount': 10000,
  'currency': 'PHP',
  'description': '',
  'statement_descriptor': '',
  'source': {
    'id': 'tok_...',
    'type': 'token'
  }
})

# retrieve payment
payment = paymongo.Payment.retrieve('payment_id')
```
### Pre-request Configuration
Configure individual requests with keyword arguments. Right now this sdk can only support keyword argument `api_key`. 

```python
import paymongo

paymongo.Payment.create({<payment_details>}, api_key='sk_test_...')
```

### Token
```python
import paymongo

# create a token
paymongo.Token.create(
  card={
    'number': '4242424242424242',
    'exp_month': 1,
    'exp_year': 22,
    'cvc': '201',
  },
  api_key='pk_test_...'
)

# retrieve_token
paymongo.Token.retrieve(id, api_key)

```


### Payment
```python
import paymongo

# create a payment
paymongo.Payment.create({
  'amount': 10000,
  'currency': 'PHP',
  'description': '',
  'statement_descriptor': '',
  'source': {
    'id': 'tok_...',
    'type': 'token'
  }
}, api_key='pk_test_...')


# retrieve a payment
paymongo.Payment.retrieve(id, api_key)

```

### Accessing Attributes
Payment and Token object attributes can be access by:
```
payment = paymongo.Payment.create(...)

# via top-level attribute
$ payment.amount
> 10000

# via `attributes` attribute
$ payment.attributes.amount
> 10000

# via dictionary / json
$ payment = payment.json()
$ payment.get('attributes').get('amount')
```

### Development
This project uses poetry: a python dependency package tool. [[installation]](https://github.com/sdispater/poetry#installation)

Run the following command to create and/or activate python virtual environment:
```
poetry shell
```

The testsuite uses pytest and pytest-cov. Run test scripts and show code coverage:
```
pytest --cov=paymongo
```
