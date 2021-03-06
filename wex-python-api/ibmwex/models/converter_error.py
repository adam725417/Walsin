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


class ConverterError(object):
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
        'converter_name': 'str',
        'error_message': 'str',
        'occurred_time': 'int',
        'uri': 'str'
    }

    attribute_map = {
        'converter_name': 'converterName',
        'error_message': 'errorMessage',
        'occurred_time': 'occurredTime',
        'uri': 'uri'
    }

    def __init__(self, converter_name=None, error_message=None, occurred_time=None, uri=None):
        """
        ConverterError - a model defined in Swagger
        """

        self._converter_name = None
        self._error_message = None
        self._occurred_time = None
        self._uri = None

        if converter_name is not None:
          self.converter_name = converter_name
        if error_message is not None:
          self.error_message = error_message
        if occurred_time is not None:
          self.occurred_time = occurred_time
        if uri is not None:
          self.uri = uri

    @property
    def converter_name(self):
        """
        Gets the converter_name of this ConverterError.

        :return: The converter_name of this ConverterError.
        :rtype: str
        """
        return self._converter_name

    @converter_name.setter
    def converter_name(self, converter_name):
        """
        Sets the converter_name of this ConverterError.

        :param converter_name: The converter_name of this ConverterError.
        :type: str
        """

        self._converter_name = converter_name

    @property
    def error_message(self):
        """
        Gets the error_message of this ConverterError.

        :return: The error_message of this ConverterError.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this ConverterError.

        :param error_message: The error_message of this ConverterError.
        :type: str
        """

        self._error_message = error_message

    @property
    def occurred_time(self):
        """
        Gets the occurred_time of this ConverterError.

        :return: The occurred_time of this ConverterError.
        :rtype: int
        """
        return self._occurred_time

    @occurred_time.setter
    def occurred_time(self, occurred_time):
        """
        Sets the occurred_time of this ConverterError.

        :param occurred_time: The occurred_time of this ConverterError.
        :type: int
        """

        self._occurred_time = occurred_time

    @property
    def uri(self):
        """
        Gets the uri of this ConverterError.

        :return: The uri of this ConverterError.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ConverterError.

        :param uri: The uri of this ConverterError.
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, ConverterError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
