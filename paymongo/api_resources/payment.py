from .common import Attribute, Base


class Payout(Base):
    def __init__(self, data):
        self.id = data.get('id')
        self.type = data.get('type')


class Source(Base):
    def __init__(self, data):
        self.id = data.get('id')
        self.type = data.get('type')


class Relationship(Base):
    def __init__(self, data):
        payout = data.get('payout')
        source = data.get('source')

        if payout.get('data'):
            self.payout = Payout(payout.get('data'))

        if source.get('data'):
            self.source = Source(source.get('data'))


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

        self.relationships = Relationship(data.get('relationships'))

    def json(self):
        return self.dict
