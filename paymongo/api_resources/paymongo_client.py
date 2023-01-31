import json
import requests
from ast import literal_eval
from paymongo import StandardException

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
      raise StandardException(PaymongoClient.get_error_detail(response=response))

    return response.json()

  def get_error_detail(response):
    response_content = response._content
    response_content_in_bytes = response_content.decode('utf-8')
    content = literal_eval(response_content_in_bytes)

    return content['errors'][0]['detail']


  def get_response(config, method, params, uri):
    headers = {
      'Authorization' : f'Basic {config.api_key}',
      'Content-Type': 'application/json',
    }

    if(method == 'get'):
      response = requests.get(headers=headers, url=uri)

    elif(method == 'post'):
      modified_params = { 'data' : { 'attributes' : params } }
      response = requests.post(data=json.dumps(modified_params), headers=headers, url=uri)

    return response

  def is_successful(response):
    return response.status_code == 200
