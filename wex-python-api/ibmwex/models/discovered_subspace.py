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


class DiscoveredSubspace(object):
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
        'available_as_crawl_space': 'bool',
        'available_as_node_space': 'bool',
        'filters': 'list[ConfigurationParameter]',
        'label': 'str',
        'name': 'str',
        'path': 'list[str]'
    }

    attribute_map = {
        'available_as_crawl_space': 'availableAsCrawlSpace',
        'available_as_node_space': 'availableAsNodeSpace',
        'filters': 'filters',
        'label': 'label',
        'name': 'name',
        'path': 'path'
    }

    def __init__(self, available_as_crawl_space=None, available_as_node_space=None, filters=None, label=None, name=None, path=None):
        """
        DiscoveredSubspace - a model defined in Swagger
        """

        self._available_as_crawl_space = None
        self._available_as_node_space = None
        self._filters = None
        self._label = None
        self._name = None
        self._path = None

        if available_as_crawl_space is not None:
          self.available_as_crawl_space = available_as_crawl_space
        if available_as_node_space is not None:
          self.available_as_node_space = available_as_node_space
        if filters is not None:
          self.filters = filters
        if label is not None:
          self.label = label
        if name is not None:
          self.name = name
        if path is not None:
          self.path = path

    @property
    def available_as_crawl_space(self):
        """
        Gets the available_as_crawl_space of this DiscoveredSubspace.

        :return: The available_as_crawl_space of this DiscoveredSubspace.
        :rtype: bool
        """
        return self._available_as_crawl_space

    @available_as_crawl_space.setter
    def available_as_crawl_space(self, available_as_crawl_space):
        """
        Sets the available_as_crawl_space of this DiscoveredSubspace.

        :param available_as_crawl_space: The available_as_crawl_space of this DiscoveredSubspace.
        :type: bool
        """

        self._available_as_crawl_space = available_as_crawl_space

    @property
    def available_as_node_space(self):
        """
        Gets the available_as_node_space of this DiscoveredSubspace.

        :return: The available_as_node_space of this DiscoveredSubspace.
        :rtype: bool
        """
        return self._available_as_node_space

    @available_as_node_space.setter
    def available_as_node_space(self, available_as_node_space):
        """
        Sets the available_as_node_space of this DiscoveredSubspace.

        :param available_as_node_space: The available_as_node_space of this DiscoveredSubspace.
        :type: bool
        """

        self._available_as_node_space = available_as_node_space

    @property
    def filters(self):
        """
        Gets the filters of this DiscoveredSubspace.

        :return: The filters of this DiscoveredSubspace.
        :rtype: list[ConfigurationParameter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """
        Sets the filters of this DiscoveredSubspace.

        :param filters: The filters of this DiscoveredSubspace.
        :type: list[ConfigurationParameter]
        """

        self._filters = filters

    @property
    def label(self):
        """
        Gets the label of this DiscoveredSubspace.

        :return: The label of this DiscoveredSubspace.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this DiscoveredSubspace.

        :param label: The label of this DiscoveredSubspace.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this DiscoveredSubspace.

        :return: The name of this DiscoveredSubspace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DiscoveredSubspace.

        :param name: The name of this DiscoveredSubspace.
        :type: str
        """

        self._name = name

    @property
    def path(self):
        """
        Gets the path of this DiscoveredSubspace.

        :return: The path of this DiscoveredSubspace.
        :rtype: list[str]
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this DiscoveredSubspace.

        :param path: The path of this DiscoveredSubspace.
        :type: list[str]
        """

        self._path = path

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
        if not isinstance(other, DiscoveredSubspace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other