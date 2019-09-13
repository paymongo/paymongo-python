from .common import Attribute, Base


class Payment(Base):
    def __init__(self, data):
        self._dict = data

        self.id = data['id']
        self.type = data['type']
        attributes = data['attributes']

        self.attributes = Attribute(attributes)

        self.amount = attributes.get('amount')
        self.currency = attributes.get('currency')
        self.description = attributes.get('description')
        self.external_reference_number = attributes.get(
            'external_reference_number')
        self.fee = attributes.get('fee')
        self.livemode = attributes.get('livemode')
        self.net_amount = attributes.get('net_amount')
        self.statement_descriptor = attributes.get('statement_descriptor')
        self.status = attributes.get('status')

    def json(self):
        return self.dict
