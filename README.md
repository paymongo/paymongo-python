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
