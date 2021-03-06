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


class Stats(object):
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
        'count': 'Number',
        'max': 'Number',
        'min': 'Number',
        'sum': 'Number',
        'cardinality': 'Number'
    }

    attribute_map = {
        'count': 'count',
        'max': 'max',
        'min': 'min',
        'sum': 'sum',
        'cardinality': 'cardinality'
    }

    def __init__(self, count=None, max=None, min=None, sum=None, cardinality=None):
        """
        Stats - a model defined in Swagger
        """

        self._count = None
        self._max = None
        self._min = None
        self._sum = None
        self._cardinality = None

        if count is not None:
          self.count = count
        if max is not None:
          self.max = max
        if min is not None:
          self.min = min
        if sum is not None:
          self.sum = sum
        if cardinality is not None:
          self.cardinality = cardinality

    @property
    def count(self):
        """
        Gets the count of this Stats.

        :return: The count of this Stats.
        :rtype: Number
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this Stats.

        :param count: The count of this Stats.
        :type: Number
        """

        self._count = count

    @property
    def max(self):
        """
        Gets the max of this Stats.

        :return: The max of this Stats.
        :rtype: Number
        """
        return self._max

    @max.setter
    def max(self, max):
        """
        Sets the max of this Stats.

        :param max: The max of this Stats.
        :type: Number
        """

        self._max = max

    @property
    def min(self):
        """
        Gets the min of this Stats.

        :return: The min of this Stats.
        :rtype: Number
        """
        return self._min

    @min.setter
    def min(self, min):
        """
        Sets the min of this Stats.

        :param min: The min of this Stats.
        :type: Number
        """

        self._min = min

    @property
    def sum(self):
        """
        Gets the sum of this Stats.

        :return: The sum of this Stats.
        :rtype: Number
        """
        return self._sum

    @sum.setter
    def sum(self, sum):
        """
        Sets the sum of this Stats.

        :param sum: The sum of this Stats.
        :type: Number
        """

        self._sum = sum

    @property
    def cardinality(self):
        """
        Gets the cardinality of this Stats.

        :return: The cardinality of this Stats.
        :rtype: Number
        """
        return self._cardinality

    @cardinality.setter
    def cardinality(self, cardinality):
        """
        Sets the cardinality of this Stats.

        :param cardinality: The cardinality of this Stats.
        :type: Number
        """

        self._cardinality = cardinality

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
        if not isinstance(other, Stats):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
