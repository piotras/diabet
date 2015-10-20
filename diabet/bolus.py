
class Bolus(object):
    def __init__(self, value, extended):
        self.value = value
        self.extended = extended

    def get_value(self):
        return self.value

    def get_extended_value(self):
        return self.extended

