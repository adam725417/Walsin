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


class Field(object):
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
        'name': 'str',
        'stats': 'Stats',
        'type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'stats': 'stats',
        'type': 'type'
    }

    def __init__(self, name=None, stats=None, type=None):
        """
        Field - a model defined in Swagger
        """

        self._name = None
        self._stats = None
        self._type = None

        if name is not None:
          self.name = name
        if stats is not None:
          self.stats = stats
        if type is not None:
          self.type = type

    @property
    def name(self):
        """
        Gets the name of this Field.

        :return: The name of this Field.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Field.

        :param name: The name of this Field.
        :type: str
        """

        self._name = name

    @property
    def stats(self):
        """
        Gets the stats of this Field.

        :return: The stats of this Field.
        :rtype: Stats
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        """
        Sets the stats of this Field.

        :param stats: The stats of this Field.
        :type: Stats
        """

        self._stats = stats

    @property
    def type(self):
        """
        Gets the type of this Field.

        :return: The type of this Field.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Field.

        :param type: The type of this Field.
        :type: str
        """
        allowed_values = ["String", "Long", "Double", "Date"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, Field):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
