class PaymongoError:
  def __init__(self, error):
    self.code = error['code'] if 'code' in error else None
    self.detail = error['detail']
    self.source = error['source'] if 'source' in error else None
