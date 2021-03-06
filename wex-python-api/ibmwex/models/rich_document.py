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


class RichDocument(object):
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
        'enriched': 'dict(str, list[RichField])',
        'id': 'str',
        'metadata': 'dict(str, list[object])',
        'removed': 'bool',
        'stored': 'dict(str, list[object])',
        'tag': 'str'
    }

    attribute_map = {
        'enriched': 'enriched',
        'id': 'id',
        'metadata': 'metadata',
        'removed': 'removed',
        'stored': 'stored',
        'tag': 'tag'
    }

    def __init__(self, enriched=None, id=None, metadata=None, removed=None, stored=None, tag=None):
        """
        RichDocument - a model defined in Swagger
        """

        self._enriched = None
        self._id = None
        self._metadata = None
        self._removed = None
        self._stored = None
        self._tag = None

        if enriched is not None:
          self.enriched = enriched
        if id is not None:
          self.id = id
        if metadata is not None:
          self.metadata = metadata
        if removed is not None:
          self.removed = removed
        if stored is not None:
          self.stored = stored
        if tag is not None:
          self.tag = tag

    @property
    def enriched(self):
        """
        Gets the enriched of this RichDocument.

        :return: The enriched of this RichDocument.
        :rtype: dict(str, list[RichField])
        """
        return self._enriched

    @enriched.setter
    def enriched(self, enriched):
        """
        Sets the enriched of this RichDocument.

        :param enriched: The enriched of this RichDocument.
        :type: dict(str, list[RichField])
        """

        self._enriched = enriched

    @property
    def id(self):
        """
        Gets the id of this RichDocument.

        :return: The id of this RichDocument.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RichDocument.

        :param id: The id of this RichDocument.
        :type: str
        """

        self._id = id

    @property
    def metadata(self):
        """
        Gets the metadata of this RichDocument.

        :return: The metadata of this RichDocument.
        :rtype: dict(str, list[object])
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this RichDocument.

        :param metadata: The metadata of this RichDocument.
        :type: dict(str, list[object])
        """

        self._metadata = metadata

    @property
    def removed(self):
        """
        Gets the removed of this RichDocument.

        :return: The removed of this RichDocument.
        :rtype: bool
        """
        return self._removed

    @removed.setter
    def removed(self, removed):
        """
        Sets the removed of this RichDocument.

        :param removed: The removed of this RichDocument.
        :type: bool
        """

        self._removed = removed

    @property
    def stored(self):
        """
        Gets the stored of this RichDocument.

        :return: The stored of this RichDocument.
        :rtype: dict(str, list[object])
        """
        return self._stored

    @stored.setter
    def stored(self, stored):
        """
        Sets the stored of this RichDocument.

        :param stored: The stored of this RichDocument.
        :type: dict(str, list[object])
        """

        self._stored = stored

    @property
    def tag(self):
        """
        Gets the tag of this RichDocument.

        :return: The tag of this RichDocument.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this RichDocument.

        :param tag: The tag of this RichDocument.
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
        if not isinstance(other, RichDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
