from paymongo import BaseEntity

class ListingEntity(BaseEntity):
  def __init__(self, data, has_more):
    BaseEntity.__init__(self)

    self.data = data
    self.has_more = has_more
