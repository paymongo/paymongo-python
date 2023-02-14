import json
import requests
from ast import literal_eval
from paymongo import ApiResource
from paymongo import StandardException
from paymongo import AuthenticationException
from paymongo import InvalidRequestException
from paymongo import ResourceNotFoundException

class PaymongoClient:
  def execute_request(config, method, path, params={}):
    uri = f"{config.api_base_url}//{config.api_version}//{path}"

    response = PaymongoClient.get_response(
      config=config,
      method=method,
      params=params,
      uri=uri
    )

    if not PaymongoClient.is_successful(response):
      PaymongoClient.handle_error(response=response)

    return ApiResource(response.json())

  def get_response(config, method, params, uri):
    headers = {
      'Authorization' : f'Basic {config.api_key}',
      'Content-Type': 'application/json',
    }

    if method == 'delete':
      response = requests.delete(headers=headers, url=uri)

    elif method == 'get':
      response = requests.get(headers=headers, params=params, url=uri)

    elif method == 'post':
      modified_params = { 'data' : { 'attributes' : params } }
      response = requests.post(data=json.dumps(modified_params), headers=headers, url=uri)

    elif method == 'put':
      modified_params = { 'data' : { 'attributes' : params } }
      response = requests.put(data=json.dumps(modified_params), headers=headers, url=uri)

    return response
  
  def handle_error(response):
    if response.status_code == 400:
      raise InvalidRequestException(response.json())
    elif response.status_code == 401:
      raise AuthenticationException(response.json())
    elif response.status_code == 404:
      raise ResourceNotFoundException(response.json())
    else:
      raise StandardException(response.json())

  def is_successful(response):
    return response.status_code == 200
