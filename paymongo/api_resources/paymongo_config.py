import base64

class PaymongoConfig:
  def __init__(self, api_key):
    self.api_key = PaymongoConfig.encode_api_key(api_key) if isinstance(api_key, str) else None
    self.api_base_url = 'https://api.paymongo.com'
    self.api_version = 'v1'

  def encode_api_key(api_key):
    api_key_in_bytes = api_key.encode('utf-8')
    encoded_api_key = base64.b64encode(api_key_in_bytes)

    return encoded_api_key.decode('utf-8')
