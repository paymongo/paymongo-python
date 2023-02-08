class ApiResource:
  def __init__(self, response):
    self.data = response['data'] if 'data' in response else response

    if 'attributes' in self.data:
      self.attributes = self.data['attributes']
      self.id = self.data['id']

    self.has_more = response['has_more'] if 'has_more' in response else None
