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


class ConfigFile(object):
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
        'encoded': 'bool',
        'size': 'float',
        'sha51': 'str'
    }

    attribute_map = {
        'name': 'name',
        'encoded': 'encoded',
        'size': 'size',
        'sha51': 'sha51'
    }

    def __init__(self, name=None, encoded=None, size=None, sha51=None):
        """
        ConfigFile - a model defined in Swagger
        """

        self._name = None
        self._encoded = None
        self._size = None
        self._sha51 = None

        if name is not None:
          self.name = name
        if encoded is not None:
          self.encoded = encoded
        if size is not None:
          self.size = size
        if sha51 is not None:
          self.sha51 = sha51

    @property
    def name(self):
        """
        Gets the name of this ConfigFile.
        File name

        :return: The name of this ConfigFile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConfigFile.
        File name

        :param name: The name of this ConfigFile.
        :type: str
        """

        self._name = name

    @property
    def encoded(self):
        """
        Gets the encoded of this ConfigFile.
        File is encoded while last operation or not.

        :return: The encoded of this ConfigFile.
        :rtype: bool
        """
        return self._encoded

    @encoded.setter
    def encoded(self, encoded):
        """
        Sets the encoded of this ConfigFile.
        File is encoded while last operation or not.

        :param encoded: The encoded of this ConfigFile.
        :type: bool
        """

        self._encoded = encoded

    @property
    def size(self):
        """
        Gets the size of this ConfigFile.
        File size

        :return: The size of this ConfigFile.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this ConfigFile.
        File size

        :param size: The size of this ConfigFile.
        :type: float
        """

        self._size = size

    @property
    def sha51(self):
        """
        Gets the sha51 of this ConfigFile.
        Hash of the file.

        :return: The sha51 of this ConfigFile.
        :rtype: str
        """
        return self._sha51

    @sha51.setter
    def sha51(self, sha51):
        """
        Sets the sha51 of this ConfigFile.
        Hash of the file.

        :param sha51: The sha51 of this ConfigFile.
        :type: str
        """

        self._sha51 = sha51

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
        if not isinstance(other, ConfigFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other