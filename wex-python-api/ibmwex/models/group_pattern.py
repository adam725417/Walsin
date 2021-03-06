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


class GroupPattern(object):
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
        'pattern': 'str',
        'allow': 'bool',
        'role': 'str'
    }

    attribute_map = {
        'pattern': 'pattern',
        'allow': 'allow',
        'role': 'role'
    }

    def __init__(self, pattern=None, allow=True, role=None):
        """
        GroupPattern - a model defined in Swagger
        """

        self._pattern = None
        self._allow = None
        self._role = None

        self.pattern = pattern
        if allow is not None:
          self.allow = allow
        if role is not None:
          self.role = role

    @property
    def pattern(self):
        """
        Gets the pattern of this GroupPattern.
        Patten text of java.util.regex.Pattern

        :return: The pattern of this GroupPattern.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this GroupPattern.
        Patten text of java.util.regex.Pattern

        :param pattern: The pattern of this GroupPattern.
        :type: str
        """
        if pattern is None:
            raise ValueError("Invalid value for `pattern`, must not be `None`")

        self._pattern = pattern

    @property
    def allow(self):
        """
        Gets the allow of this GroupPattern.
        true: User with group match this patten is Admin false: User with group match this patten is User 

        :return: The allow of this GroupPattern.
        :rtype: bool
        """
        return self._allow

    @allow.setter
    def allow(self, allow):
        """
        Sets the allow of this GroupPattern.
        true: User with group match this patten is Admin false: User with group match this patten is User 

        :param allow: The allow of this GroupPattern.
        :type: bool
        """

        self._allow = allow

    @property
    def role(self):
        """
        Gets the role of this GroupPattern.
        A group applied for the user mathced by the pattern. If this value is specified, 'allow' is ignored. 

        :return: The role of this GroupPattern.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this GroupPattern.
        A group applied for the user mathced by the pattern. If this value is specified, 'allow' is ignored. 

        :param role: The role of this GroupPattern.
        :type: str
        """
        allowed_values = ["Admin", "User", "ToolUser", "AppUser"]
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

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
        if not isinstance(other, GroupPattern):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
