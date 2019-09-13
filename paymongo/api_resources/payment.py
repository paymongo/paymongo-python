from .common import Base, Billing


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



class PaymentAttribute(Base):
    def __init__(self, data):
        self.amount = data.get('amount')

        if data.get('billing'):
            self.billing = Billing(data.get('billing'))

        self.currency = data.get('currency')
        self.description = data.get('description')
        self.external_reference_number = data.get(
            'external_reference_number')
        self.fee = data.get('fee')
        self.livemode = data.get('livemode')
        self.net_amount = data.get('net_amount')
        self.statement_descriptor = data.get('statement_descriptor')
        self.status = data.get('status')



class Payment(Base):
    def __init__(self, data):
        self._dict = data

        self.id = data['id']
        self.type = data['type']
        attributes = data['attributes']

        self.attributes = PaymentAttribute(attributes)

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
