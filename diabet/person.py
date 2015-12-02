# -*- coding: utf-8 -*-
import datetime
import pytz

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

    def set_timezone(self, timezone):
        """
        Set the timezone for a person.

        :param timezone: timezone to set
        :type timezone: pytz.timezone

        :raises: ValueException in case of invalid timezone type
        """
        if not isinstance(timezone, datetime.tzinfo):
            raise ValueException('Invalid timezone type')
        self.data['timezone'] = timezone.zone

    def get_timezone(self):
        """
        Get the timezone of person.

        :returns: pytz.timezone
        :raises: ValueException in case of missinh timezone.
        """
        self._validate_key_in_data('timezone', 'Missing  timezone')
        return pytz.timezone(self.data['timezone'])

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

        :param icr: icr value whic is valid for given hour
        :param hour: an hour
        :type icr: integer
        :type hour: integer

        For example, if icr is '6' and hour is 9, it means that '6' basal rate starts at
        9:00 (9am) and last till 10:00 (10am).

        :raises: ValueException in case of invalid icr or hour
        """
        if icr < 1:
            raise ValueException('Invalid icr value. Should be larger than 1.')
        if hour < 1 or hour > 24:
            raise ValueException('Invalid hour')
        # initialize icr if it's not set yet
        if 'icr' not in self.data:
            self.data['icr'] = {}
        self.data['icr'][str(hour)] = icr

    def get_icr_at(self, hour):
        """
        Get icr at given hour.

        :param hour: an hour in 24 hour format [0-23]
        :type hour: integer

        :raises: ValueException in case of invalid hour
        """
        if hour < 1 or hour > 24:
            raise ValueException('Invalid hour')

        strhour = str(hour)
        if 'icr' not in self.data or strhour not in self.data['icr']:
            return self.get_default_icr()
        return self.data['icr'][strhour]

    def set_default_isf(self, isf):
        """
        Set default Insulin Sensivity Factor.

        http://www.diabetesselfmanagement.com/diabetes-resources/definitions/insulin-sensitivity-factor/

        If your Blood Glucose level is 70 and you take one unit of insulin, and BG level is 100 after that,
        then your ISF is 30.

        :raises: ValueException in case of invalid isf.
        """
        if isf < 1:
            raise ValueException('Invalid negative value of isf.')
        self.data['default_isf'] = isf

    def get_default_isf(self):
        """
        Get default isf.

        """
        self._validate_key_in_data('default_isf', 'Missing default isf')
        return self.data['default_isf']

    def set_measure_mg(self, flag):
        """
        Set mg/dL as to measure blood glucose.

        :param flag: True for mg/dL, False for mmol/L
        """
        self.data['measure_mg'] = flag

    def has_measure_mg(self):
        """
        Check if person has mg/dL set for blood glucose measuring.

        """
        return self.data['measure_mg']
