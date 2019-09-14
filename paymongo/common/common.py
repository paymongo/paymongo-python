class Base:
    def __str__(self):
        return self._get_object_attributes()

    def __repr__(self):
        return self._get_object_attributes()

    def _get_object_attributes(self):
        attrs = vars(self)
        attributes = ', '.join("%s=%s" % item for item in attrs.items()
                               if not item[0].startswith('_'))
        return '{object}({attributes})'.format(object=self.__class__.__name__,
                                               attributes=attributes)


class Address(Base):
    def __init__(self, data):
        self.city = data.get('city')
        self.country = data.get('country')
        self.line1 = data.get('line1')
        self.line2 = data.get('line2')
        self.postal_code = data.get('postal_code')
        self.state = data.get('state')


class Billing(Base):
    def __init__(self, data):

        if data.get('address'):
            self.address = Address(data.get('address'))

        self.name = data.get('name')
        self.email = data.get('email')
        self.phone = data.get('phone')
