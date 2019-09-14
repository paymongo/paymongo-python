from .common import Base


class Card(Base):
    def __init__(self, data):
        self.address_city = data.get('address_city')
        self.address_country = data.get('address_country')
        self.address_line1 = data.get('address_line1')
        self.address_line2 = data.get('address_line2')
        self.address_zip = data.get('address_zip')
        self.brand = data.get('brand')
        self.country = data.get('country')
        self.exp_year = data.get('exp_year')
        self.last4 = data.get('last4')


class TokenAttribute(Base):
    def __init__(self, data):
        self.card = Card(data.get('card'))
        self.created = data.get('created')
        self.kind = data.get('kind')
        self.livemode = data.get('livemode')
        self.updated = data.get('updated')
        self.used = data.get('used')


class Token(Base):
    def __init__(self, data):
        self._dict = data

        self.id = data['id']
        self.type = data['type']
        attributes = data['attributes']

        self.attributes = TokenAttribute(attributes)

        self.card = Card(attributes.get('card'))
        self.created = attributes.get('created')
        self.kind = attributes.get('kind')
        self.livemode = attributes.get('livemode')
        self.updated = data.get('updated')
        self.used = data.get('used')

    def json(self):
        return self._dict
