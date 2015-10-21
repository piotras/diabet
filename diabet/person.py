# -*- coding: utf-8 -*-

from errors import ValueException

class Person(object):
    def __init__(self, data={}):
        self.data = data

    def _validate_key_in_data(self, key, error):
        if key not in self.data:
            raise ValueException(error)

    def get_name(self):
        """
        Get the name of the person.

        :returns: name of the person
        :raises: ValueException on error
        """
        self._validate_key_in_data('name', 'Missing name of the person')
        return self.data['name']

    def set_default_basal_rate(self, rate):
        """
        Sets default basal rate.

        Basal Rate: The rate at which an insulin pump infuses small, "background" doses of short-acting insulin.
        http://www.diabetesselfmanagement.com/diabetes-resources/definitions/basal-rate/

        Basal rate 0 is allowed because person might not have insulin pump.
        With traditional injections, basal rate can not be set.

        :raises: ValueException in case of invalid rate.
        """
        if rate < 0:
            raise ValueException('Invalid, negative value of basal rate')
        self.data['default_basal_rate'] = rate

    def get_default_basal_rate(self):
        """
        Get default basal rate.

        :raises: ValueException in case of invalid value.
        """
        self._validate_key_in_data('default_basal_rate', 'Missing  default_basal_rate')
        return self.data['default_basal_rate']

    def set_basal_rate_at(self, rate, hour):
        """
        Set basal rate for given hour.
        Basal rate starts at given hour and lasts for next hour.

        For example, if rate is '0,6' and hour is 14, it means that '0,6' basal rate starts at
        14 (2pm) and last till 15 (3pm).

        :raises: ValueException in case of invalid rate or hour
        """
        if rate < 0:
            raise ValueException('Invalid, negative value of basal rate')
        if hour < 1 or hour > 24:
            raise ValueException('Invalid hour')
        # initialize basal rate if it's not set yet
        if 'basal_rate' not in self.data:
            self.data['basal_rate'] = {}
        self.data['basal_rate'][hour] = rate

    def get_basal_rate_at(self, hour):
        """
        Get basal rate at given hour.

        :raises: ValueException in case of invalid hour
        """
        if hour < 1 or hour > 24:
            raise ValueException('Invalid hour')
        if 'basal_rate' not in self.data or hour not in self.data['basal_rate']:
            return self.get_default_basal_rate()
        return self.data['basal_rate'][hour]

    def set_bg_raise_level(self, level):
        raise NotImplementedError()

    def get_bg_raise_level(self):
        raise NotImplementedError()

    def set_default_icr(self, icr):
        """
        Set default icr.

        Insulin-to-Carbohydrate Ratio
        A ratio that specifies the number of grams of carbohydrate covered by each unit of rapid- or short-acting insulin.
        This ratio serves as the foundation for adjusting premeal bolus insulin doses.

        http://www.diabetesselfmanagement.com/diabetes-resources/definitions/insulin-to-carbohydrate-ratio/

        :raises: ValueException in case of invalid icr.
        """
        if icr < 1:
            raise ValueException('Invalid icr value. Should be larger then 1.')
        self.data['default_icr'] = icr

    def get_default_icr(self):
        """
        Get default icr.

        """
        self._validate_key_in_data('default_icr', 'Missing default icr')
        return self.data['default_icr']

    def set_icr_at(self, icr, hour):
        """
        Set icr for given hour.
        icr starts at given hour and lasts for next hour.

        For example, if icr is '0,6' and hour is 9, it means that '0,6' basal rate starts at
        9 (9am) and last till 10 (10am).

        :raises: ValueException in case of invalid icr or hour
        """
        if icr < 1:
            raise ValueException('Invalid icr value. Should be larger than 1.')
        if hour < 1 or hour > 24:
            raise ValueException('Invalid hour')
        # initialize icr if it's not set yet
        if 'icr' not in self.data:
            self.data['icr'] = {}
        self.data['icr'][hour] = icr

    def get_icr_at(self, hour):
        """
        Get icr at given hour.

        :raises: ValueException in case of invalid hour
        """
        if hour < 1 or hour > 24:
            raise ValueException('Invalid hour')
        if 'icr' not in self.data or hour not in self.data['icr']:
            return self.get_default_icr()
        return self.data['icr'][hour]
