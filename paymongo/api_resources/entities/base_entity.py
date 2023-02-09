class BaseEntity:
  def __init__(self) -> None:
    pass

  def get_value(self, array, index):
    return array[index] if index in array else ''
