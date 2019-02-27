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


class ConverterPipelineConfiguration(object):
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
        'converter_configurations': 'list[ConverterConfiguration]'
    }

    attribute_map = {
        'converter_configurations': 'converterConfigurations'
    }

    def __init__(self, converter_configurations=None):
        """
        ConverterPipelineConfiguration - a model defined in Swagger
        """

        self._converter_configurations = None

        if converter_configurations is not None:
          self.converter_configurations = converter_configurations

    @property
    def converter_configurations(self):
        """
        Gets the converter_configurations of this ConverterPipelineConfiguration.

        :return: The converter_configurations of this ConverterPipelineConfiguration.
        :rtype: list[ConverterConfiguration]
        """
        return self._converter_configurations

    @converter_configurations.setter
    def converter_configurations(self, converter_configurations):
        """
        Sets the converter_configurations of this ConverterPipelineConfiguration.

        :param converter_configurations: The converter_configurations of this ConverterPipelineConfiguration.
        :type: list[ConverterConfiguration]
        """

        self._converter_configurations = converter_configurations

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
        if not isinstance(other, ConverterPipelineConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
