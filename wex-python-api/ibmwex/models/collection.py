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


class Collection(object):
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
        'category': 'Category',
        'datasets': 'list[str]',
        'description': 'str',
        'enrich_field_groups': 'list[EnrichFieldGroup]',
        'enrichments': 'list[str]',
        'id': 'str',
        'metadata': 'Metadata',
        'name': 'str',
        'num_replicas': 'int',
        'num_shards': 'int',
        'rich_datasets': 'list[str]',
        'params': 'CollectionParams',
        'tags': 'dict(str, object)'
    }

    attribute_map = {
        'category': 'category',
        'datasets': 'datasets',
        'description': 'description',
        'enrich_field_groups': 'enrichFieldGroups',
        'enrichments': 'enrichments',
        'id': 'id',
        'metadata': 'metadata',
        'name': 'name',
        'num_replicas': 'numReplicas',
        'num_shards': 'numShards',
        'rich_datasets': 'richDatasets',
        'params': 'params',
        'tags': 'tags'
    }

    def __init__(self, category=None, datasets=None, description=None, enrich_field_groups=None, enrichments=None, id=None, metadata=None, name=None, num_replicas=1, num_shards=1, rich_datasets=None, params=None, tags=None):
        """
        Collection - a model defined in Swagger
        """

        self._category = None
        self._datasets = None
        self._description = None
        self._enrich_field_groups = None
        self._enrichments = None
        self._id = None
        self._metadata = None
        self._name = None
        self._num_replicas = None
        self._num_shards = None
        self._rich_datasets = None
        self._params = None
        self._tags = None

        if category is not None:
          self.category = category
        if datasets is not None:
          self.datasets = datasets
        if description is not None:
          self.description = description
        if enrich_field_groups is not None:
          self.enrich_field_groups = enrich_field_groups
        if enrichments is not None:
          self.enrichments = enrichments
        if id is not None:
          self.id = id
        if metadata is not None:
          self.metadata = metadata
        if name is not None:
          self.name = name
        if num_replicas is not None:
          self.num_replicas = num_replicas
        if num_shards is not None:
          self.num_shards = num_shards
        if rich_datasets is not None:
          self.rich_datasets = rich_datasets
        if params is not None:
          self.params = params
        if tags is not None:
          self.tags = tags

    @property
    def category(self):
        """
        Gets the category of this Collection.

        :return: The category of this Collection.
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this Collection.

        :param category: The category of this Collection.
        :type: Category
        """

        self._category = category

    @property
    def datasets(self):
        """
        Gets the datasets of this Collection.

        :return: The datasets of this Collection.
        :rtype: list[str]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """
        Sets the datasets of this Collection.

        :param datasets: The datasets of this Collection.
        :type: list[str]
        """

        self._datasets = datasets

    @property
    def description(self):
        """
        Gets the description of this Collection.

        :return: The description of this Collection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Collection.

        :param description: The description of this Collection.
        :type: str
        """

        self._description = description

    @property
    def enrich_field_groups(self):
        """
        Gets the enrich_field_groups of this Collection.

        :return: The enrich_field_groups of this Collection.
        :rtype: list[EnrichFieldGroup]
        """
        return self._enrich_field_groups

    @enrich_field_groups.setter
    def enrich_field_groups(self, enrich_field_groups):
        """
        Sets the enrich_field_groups of this Collection.

        :param enrich_field_groups: The enrich_field_groups of this Collection.
        :type: list[EnrichFieldGroup]
        """

        self._enrich_field_groups = enrich_field_groups

    @property
    def enrichments(self):
        """
        Gets the enrichments of this Collection.

        :return: The enrichments of this Collection.
        :rtype: list[str]
        """
        return self._enrichments

    @enrichments.setter
    def enrichments(self, enrichments):
        """
        Sets the enrichments of this Collection.

        :param enrichments: The enrichments of this Collection.
        :type: list[str]
        """

        self._enrichments = enrichments

    @property
    def id(self):
        """
        Gets the id of this Collection.

        :return: The id of this Collection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Collection.

        :param id: The id of this Collection.
        :type: str
        """

        self._id = id

    @property
    def metadata(self):
        """
        Gets the metadata of this Collection.

        :return: The metadata of this Collection.
        :rtype: Metadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this Collection.

        :param metadata: The metadata of this Collection.
        :type: Metadata
        """

        self._metadata = metadata

    @property
    def name(self):
        """
        Gets the name of this Collection.

        :return: The name of this Collection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Collection.

        :param name: The name of this Collection.
        :type: str
        """

        self._name = name

    @property
    def num_replicas(self):
        """
        Gets the num_replicas of this Collection.

        :return: The num_replicas of this Collection.
        :rtype: int
        """
        return self._num_replicas

    @num_replicas.setter
    def num_replicas(self, num_replicas):
        """
        Sets the num_replicas of this Collection.

        :param num_replicas: The num_replicas of this Collection.
        :type: int
        """
        if num_replicas is not None and num_replicas < 1:
            raise ValueError("Invalid value for `num_replicas`, must be a value greater than or equal to `1`")

        self._num_replicas = num_replicas

    @property
    def num_shards(self):
        """
        Gets the num_shards of this Collection.

        :return: The num_shards of this Collection.
        :rtype: int
        """
        return self._num_shards

    @num_shards.setter
    def num_shards(self, num_shards):
        """
        Sets the num_shards of this Collection.

        :param num_shards: The num_shards of this Collection.
        :type: int
        """
        if num_shards is not None and num_shards < 1:
            raise ValueError("Invalid value for `num_shards`, must be a value greater than or equal to `1`")

        self._num_shards = num_shards

    @property
    def rich_datasets(self):
        """
        Gets the rich_datasets of this Collection.

        :return: The rich_datasets of this Collection.
        :rtype: list[str]
        """
        return self._rich_datasets

    @rich_datasets.setter
    def rich_datasets(self, rich_datasets):
        """
        Sets the rich_datasets of this Collection.

        :param rich_datasets: The rich_datasets of this Collection.
        :type: list[str]
        """

        self._rich_datasets = rich_datasets

    @property
    def params(self):
        """
        Gets the params of this Collection.

        :return: The params of this Collection.
        :rtype: CollectionParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """
        Sets the params of this Collection.

        :param params: The params of this Collection.
        :type: CollectionParams
        """

        self._params = params

    @property
    def tags(self):
        """
        Gets the tags of this Collection.

        :return: The tags of this Collection.
        :rtype: dict(str, object)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Collection.

        :param tags: The tags of this Collection.
        :type: dict(str, object)
        """

        self._tags = tags

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
        if not isinstance(other, Collection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
