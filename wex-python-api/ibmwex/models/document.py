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


class Document(object):
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
        'fields': 'MultiFieldMap',
        'group_id': 'str',
        'id': 'str',
        'metadata': 'MultiFieldMap',
        'removed': 'bool',
        'tag': 'str'
    }

    attribute_map = {
        'fields': 'fields',
        'group_id': 'groupId',
        'id': 'id',
        'metadata': 'metadata',
        'removed': 'removed',
        'tag': 'tag'
    }

    def __init__(self, fields=None, group_id=None, id=None, metadata=None, removed=None, tag=None):
        """
        Document - a model defined in Swagger
        """

        self._fields = None
        self._group_id = None
        self._id = None
        self._metadata = None
        self._removed = None
        self._tag = None

        if fields is not None:
          self.fields = fields
        if group_id is not None:
          self.group_id = group_id
        if id is not None:
          self.id = id
        if metadata is not None:
          self.metadata = metadata
        if removed is not None:
          self.removed = removed
        if tag is not None:
          self.tag = tag

    @property
    def fields(self):
        """
        Gets the fields of this Document.

        :return: The fields of this Document.
        :rtype: MultiFieldMap
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this Document.

        :param fields: The fields of this Document.
        :type: MultiFieldMap
        """

        self._fields = fields

    @property
    def group_id(self):
        """
        Gets the group_id of this Document.

        :return: The group_id of this Document.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this Document.

        :param group_id: The group_id of this Document.
        :type: str
        """

        self._group_id = group_id

    @property
    def id(self):
        """
        Gets the id of this Document.

        :return: The id of this Document.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Document.

        :param id: The id of this Document.
        :type: str
        """

        self._id = id

    @property
    def metadata(self):
        """
        Gets the metadata of this Document.

        :return: The metadata of this Document.
        :rtype: MultiFieldMap
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Document.

        :param metadata: The metadata of this Document.
        :type: MultiFieldMap
        """

        self._metadata = metadata

    @property
    def removed(self):
        """
        Gets the removed of this Document.

        :return: The removed of this Document.
        :rtype: bool
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """
        Sets the removed of this Document.

        :param removed: The removed of this Document.
        :type: bool
        """

        self._removed = removed

    @property
    def tag(self):
        """
        Gets the tag of this Document.

        :return: The tag of this Document.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this Document.

        :param tag: The tag of this Document.
        :type: str
        """

        self._tag = tag

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
        if not isinstance(other, Document):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
