# Paymongo Python SDK

## Usage

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
