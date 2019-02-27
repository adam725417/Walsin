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


class SystemUsageNlpMetrics(object):
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
        'total_count': 'int',
        'total_input_size': 'int',
        'total_output_size': 'int',
        'collections': 'list[SystemUsageNlpMetricsCollections]'
    }

    attribute_map = {
        'total_count': 'totalCount',
        'total_input_size': 'totalInputSize',
        'total_output_size': 'totalOutputSize',
        'collections': 'collections'
    }

    def __init__(self, total_count=None, total_input_size=None, total_output_size=None, collections=None):
        """
        SystemUsageNlpMetrics - a model defined in Swagger
        """

        self._total_count = None
        self._total_input_size = None
        self._total_output_size = None
        self._collections = None

        if total_count is not None:
          self.total_count = total_count
        if total_input_size is not None:
          self.total_input_size = total_input_size
        if total_output_size is not None:
          self.total_output_size = total_output_size
        if collections is not None:
          self.collections = collections

    @property
    def total_count(self):
        """
        Gets the total_count of this SystemUsageNlpMetrics.

        :return: The total_count of this SystemUsageNlpMetrics.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this SystemUsageNlpMetrics.

        :param total_count: The total_count of this SystemUsageNlpMetrics.
        :type: int
        """

        self._total_count = total_count

    @property
    def total_input_size(self):
        """
        Gets the total_input_size of this SystemUsageNlpMetrics.

        :return: The total_input_size of this SystemUsageNlpMetrics.
        :rtype: int
        """
        return self._total_input_size

    @total_input_size.setter
    def total_input_size(self, total_input_size):
        """
        Sets the total_input_size of this SystemUsageNlpMetrics.

        :param total_input_size: The total_input_size of this SystemUsageNlpMetrics.
        :type: int
        """

        self._total_input_size = total_input_size

    @property
    def total_output_size(self):
        """
        Gets the total_output_size of this SystemUsageNlpMetrics.

        :return: The total_output_size of this SystemUsageNlpMetrics.
        :rtype: int
        """
        return self._total_output_size

    @total_output_size.setter
    def total_output_size(self, total_output_size):
        """
        Sets the total_output_size of this SystemUsageNlpMetrics.

        :param total_output_size: The total_output_size of this SystemUsageNlpMetrics.
        :type: int
        """

        self._total_output_size = total_output_size

    @property
    def collections(self):
        """
        Gets the collections of this SystemUsageNlpMetrics.

        :return: The collections of this SystemUsageNlpMetrics.
        :rtype: list[SystemUsageNlpMetricsCollections]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """
        Sets the collections of this SystemUsageNlpMetrics.

        :param collections: The collections of this SystemUsageNlpMetrics.
        :type: list[SystemUsageNlpMetricsCollections]
        """

        self._collections = collections

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
        if not isinstance(other, SystemUsageNlpMetrics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other