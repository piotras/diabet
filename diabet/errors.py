
class DiabetException(Exception):
    error = 'General exception'

class ValueException(Exception):
    error = 'Invalid value'

class NoSuchPersonException(Exception):
    error = 'No such person'
