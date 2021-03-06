# coding: utf-8

"""
    WEX REST APIs

    Authentication methods - Basic Auth - JSON Web Token   - [POST /api/v1/usermgmt/login](#!/User/signinUser)   - [POST /api/v1/usermgmt/logout](#!/User/doLogout) - Python client sample [Download](/docs/wex-python-api.zip) 

    OpenAPI spec version: 12.0.2.417
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Schedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enabled': 'bool',
        'schedule_type': 'str',
        'start_on': 'str',
        'update_interval': 'UpdateInterval'
    }

    attribute_map = {
        'enabled': 'enabled',
        'schedule_type': 'scheduleType',
        'start_on': 'startOn',
        'update_interval': 'updateInterval'
    }

    def __init__(self, enabled=None, schedule_type=None, start_on=None, update_interval=None):
        """
        Schedule - a model defined in Swagger
        """

        self._enabled = None
        self._schedule_type = None
        self._start_on = None
        self._update_interval = None

        if enabled is not None:
          self.enabled = enabled
        if schedule_type is not None:
          self.schedule_type = schedule_type
        if start_on is not None:
          self.start_on = start_on
        if update_interval is not None:
          self.update_interval = update_interval

    @property
    def enabled(self):
        """
        Gets the enabled of this Schedule.

        :return: The enabled of this Schedule.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this Schedule.

        :param enabled: The enabled of this Schedule.
        :type: bool
        """

        self._enabled = enabled

    @property
    def schedule_type(self):
        """
        Gets the schedule_type of this Schedule.

        :return: The schedule_type of this Schedule.
        :rtype: str
        """
        return self._schedule_type

    @schedule_type.setter
    def schedule_type(self, schedule_type):
        """
        Sets the schedule_type of this Schedule.

        :param schedule_type: The schedule_type of this Schedule.
        :type: str
        """

        self._schedule_type = schedule_type

    @property
    def start_on(self):
        """
        Gets the start_on of this Schedule.

        :return: The start_on of this Schedule.
        :rtype: str
        """
        return self._start_on

    @start_on.setter
    def start_on(self, start_on):
        """
        Sets the start_on of this Schedule.

        :param start_on: The start_on of this Schedule.
        :type: str
        """

        self._start_on = start_on

    @property
    def update_interval(self):
        """
        Gets the update_interval of this Schedule.

        :return: The update_interval of this Schedule.
        :rtype: UpdateInterval
        """
        return self._update_interval

    @update_interval.setter
    def update_interval(self, update_interval):
        """
        Sets the update_interval of this Schedule.

        :param update_interval: The update_interval of this Schedule.
        :type: UpdateInterval
        """

        self._update_interval = update_interval

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
