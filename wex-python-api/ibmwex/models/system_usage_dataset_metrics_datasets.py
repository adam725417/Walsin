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


class SystemUsageDatasetMetricsDatasets(object):
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
        'dsid': 'str',
        'size': 'int',
        'last_update': 'int'
    }

    attribute_map = {
        'dsid': 'dsid',
        'size': 'size',
        'last_update': 'lastUpdate'
    }

    def __init__(self, dsid=None, size=None, last_update=None):
        """
        SystemUsageDatasetMetricsDatasets - a model defined in Swagger
        """

        self._dsid = None
        self._size = None
        self._last_update = None

        if dsid is not None:
          self.dsid = dsid
        if size is not None:
          self.size = size
        if last_update is not None:
          self.last_update = last_update

    @property
    def dsid(self):
        """
        Gets the dsid of this SystemUsageDatasetMetricsDatasets.

        :return: The dsid of this SystemUsageDatasetMetricsDatasets.
        :rtype: str
        """
        return self._dsid

    @dsid.setter
    def dsid(self, dsid):
        """
        Sets the dsid of this SystemUsageDatasetMetricsDatasets.

        :param dsid: The dsid of this SystemUsageDatasetMetricsDatasets.
        :type: str
        """

        self._dsid = dsid

    @property
    def size(self):
        """
        Gets the size of this SystemUsageDatasetMetricsDatasets.

        :return: The size of this SystemUsageDatasetMetricsDatasets.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SystemUsageDatasetMetricsDatasets.

        :param size: The size of this SystemUsageDatasetMetricsDatasets.
        :type: int
        """

        self._size = size

    @property
    def last_update(self):
        """
        Gets the last_update of this SystemUsageDatasetMetricsDatasets.

        :return: The last_update of this SystemUsageDatasetMetricsDatasets.
        :rtype: int
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """
        Sets the last_update of this SystemUsageDatasetMetricsDatasets.

        :param last_update: The last_update of this SystemUsageDatasetMetricsDatasets.
        :type: int
        """

        self._last_update = last_update

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
        if not isinstance(other, SystemUsageDatasetMetricsDatasets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
