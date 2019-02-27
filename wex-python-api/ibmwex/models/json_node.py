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


class JsonNode(object):
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
        'array': 'bool',
        'big_decimal': 'bool',
        'big_integer': 'bool',
        'binary': 'bool',
        'boolean': 'bool',
        'container_node': 'bool',
        'double': 'bool',
        'float': 'bool',
        'floating_point_number': 'bool',
        'int': 'bool',
        'integral_number': 'bool',
        'long': 'bool',
        'missing_node': 'bool',
        'node_type': 'str',
        'null': 'bool',
        'number': 'bool',
        'object': 'bool',
        'pojo': 'bool',
        'short': 'bool',
        'textual': 'bool',
        'value_node': 'bool'
    }

    attribute_map = {
        'array': 'array',
        'big_decimal': 'bigDecimal',
        'big_integer': 'bigInteger',
        'binary': 'binary',
        'boolean': 'boolean',
        'container_node': 'containerNode',
        'double': 'double',
        'float': 'float',
        'floating_point_number': 'floatingPointNumber',
        'int': 'int',
        'integral_number': 'integralNumber',
        'long': 'long',
        'missing_node': 'missingNode',
        'node_type': 'nodeType',
        'null': 'null',
        'number': 'number',
        'object': 'object',
        'pojo': 'pojo',
        'short': 'short',
        'textual': 'textual',
        'value_node': 'valueNode'
    }

    def __init__(self, array=None, big_decimal=None, big_integer=None, binary=None, boolean=None, container_node=None, double=None, float=None, floating_point_number=None, int=None, integral_number=None, long=None, missing_node=None, node_type=None, null=None, number=None, object=None, pojo=None, short=None, textual=None, value_node=None):
        """
        JsonNode - a model defined in Swagger
        """

        self._array = None
        self._big_decimal = None
        self._big_integer = None
        self._binary = None
        self._boolean = None
        self._container_node = None
        self._double = None
        self._float = None
        self._floating_point_number = None
        self._int = None
        self._integral_number = None
        self._long = None
        self._missing_node = None
        self._node_type = None
        self._null = None
        self._number = None
        self._object = None
        self._pojo = None
        self._short = None
        self._textual = None
        self._value_node = None

        if array is not None:
          self.array = array
        if big_decimal is not None:
          self.big_decimal = big_decimal
        if big_integer is not None:
          self.big_integer = big_integer
        if binary is not None:
          self.binary = binary
        if boolean is not None:
          self.boolean = boolean
        if container_node is not None:
          self.container_node = container_node
        if double is not None:
          self.double = double
        if float is not None:
          self.float = float
        if floating_point_number is not None:
          self.floating_point_number = floating_point_number
        if int is not None:
          self.int = int
        if integral_number is not None:
          self.integral_number = integral_number
        if long is not None:
          self.long = long
        if missing_node is not None:
          self.missing_node = missing_node
        if node_type is not None:
          self.node_type = node_type
        if null is not None:
          self.null = null
        if number is not None:
          self.number = number
        if object is not None:
          self.object = object
        if pojo is not None:
          self.pojo = pojo
        if short is not None:
          self.short = short
        if textual is not None:
          self.textual = textual
        if value_node is not None:
          self.value_node = value_node

    @property
    def array(self):
        """
        Gets the array of this JsonNode.

        :return: The array of this JsonNode.
        :rtype: bool
        """
        return self._array

    @array.setter
    def array(self, array):
        """
        Sets the array of this JsonNode.

        :param array: The array of this JsonNode.
        :type: bool
        """

        self._array = array

    @property
    def big_decimal(self):
        """
        Gets the big_decimal of this JsonNode.

        :return: The big_decimal of this JsonNode.
        :rtype: bool
        """
        return self._big_decimal

    @big_decimal.setter
    def big_decimal(self, big_decimal):
        """
        Sets the big_decimal of this JsonNode.

        :param big_decimal: The big_decimal of this JsonNode.
        :type: bool
        """

        self._big_decimal = big_decimal

    @property
    def big_integer(self):
        """
        Gets the big_integer of this JsonNode.

        :return: The big_integer of this JsonNode.
        :rtype: bool
        """
        return self._big_integer

    @big_integer.setter
    def big_integer(self, big_integer):
        """
        Sets the big_integer of this JsonNode.

        :param big_integer: The big_integer of this JsonNode.
        :type: bool
        """

        self._big_integer = big_integer

    @property
    def binary(self):
        """
        Gets the binary of this JsonNode.

        :return: The binary of this JsonNode.
        :rtype: bool
        """
        return self._binary

    @binary.setter
    def binary(self, binary):
        """
        Sets the binary of this JsonNode.

        :param binary: The binary of this JsonNode.
        :type: bool
        """

        self._binary = binary

    @property
    def boolean(self):
        """
        Gets the boolean of this JsonNode.

        :return: The boolean of this JsonNode.
        :rtype: bool
        """
        return self._boolean

    @boolean.setter
    def boolean(self, boolean):
        """
        Sets the boolean of this JsonNode.

        :param boolean: The boolean of this JsonNode.
        :type: bool
        """

        self._boolean = boolean

    @property
    def container_node(self):
        """
        Gets the container_node of this JsonNode.

        :return: The container_node of this JsonNode.
        :rtype: bool
        """
        return self._container_node

    @container_node.setter
    def container_node(self, container_node):
        """
        Sets the container_node of this JsonNode.

        :param container_node: The container_node of this JsonNode.
        :type: bool
        """

        self._container_node = container_node

    @property
    def double(self):
        """
        Gets the double of this JsonNode.

        :return: The double of this JsonNode.
        :rtype: bool
        """
        return self._double

    @double.setter
    def double(self, double):
        """
        Sets the double of this JsonNode.

        :param double: The double of this JsonNode.
        :type: bool
        """

        self._double = double

    @property
    def float(self):
        """
        Gets the float of this JsonNode.

        :return: The float of this JsonNode.
        :rtype: bool
        """
        return self._float

    @float.setter
    def float(self, float):
        """
        Sets the float of this JsonNode.

        :param float: The float of this JsonNode.
        :type: bool
        """

        self._float = float

    @property
    def floating_point_number(self):
        """
        Gets the floating_point_number of this JsonNode.

        :return: The floating_point_number of this JsonNode.
        :rtype: bool
        """
        return self._floating_point_number

    @floating_point_number.setter
    def floating_point_number(self, floating_point_number):
        """
        Sets the floating_point_number of this JsonNode.

        :param floating_point_number: The floating_point_number of this JsonNode.
        :type: bool
        """

        self._floating_point_number = floating_point_number

    @property
    def int(self):
        """
        Gets the int of this JsonNode.

        :return: The int of this JsonNode.
        :rtype: bool
        """
        return self._int

    @int.setter
    def int(self, int):
        """
        Sets the int of this JsonNode.

        :param int: The int of this JsonNode.
        :type: bool
        """

        self._int = int

    @property
    def integral_number(self):
        """
        Gets the integral_number of this JsonNode.

        :return: The integral_number of this JsonNode.
        :rtype: bool
        """
        return self._integral_number

    @integral_number.setter
    def integral_number(self, integral_number):
        """
        Sets the integral_number of this JsonNode.

        :param integral_number: The integral_number of this JsonNode.
        :type: bool
        """

        self._integral_number = integral_number

    @property
    def long(self):
        """
        Gets the long of this JsonNode.

        :return: The long of this JsonNode.
        :rtype: bool
        """
        return self._long

    @long.setter
    def long(self, long):
        """
        Sets the long of this JsonNode.

        :param long: The long of this JsonNode.
        :type: bool
        """

        self._long = long

    @property
    def missing_node(self):
        """
        Gets the missing_node of this JsonNode.

        :return: The missing_node of this JsonNode.
        :rtype: bool
        """
        return self._missing_node

    @missing_node.setter
    def missing_node(self, missing_node):
        """
        Sets the missing_node of this JsonNode.

        :param missing_node: The missing_node of this JsonNode.
        :type: bool
        """

        self._missing_node = missing_node

    @property
    def node_type(self):
        """
        Gets the node_type of this JsonNode.

        :return: The node_type of this JsonNode.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        """
        Sets the node_type of this JsonNode.

        :param node_type: The node_type of this JsonNode.
        :type: str
        """
        allowed_values = ["ARRAY", "BINARY", "BOOLEAN", "MISSING", "NULL", "NUMBER", "OBJECT", "POJO", "STRING"]
        if node_type not in allowed_values:
            raise ValueError(
                "Invalid value for `node_type` ({0}), must be one of {1}"
                .format(node_type, allowed_values)
            )

        self._node_type = node_type

    @property
    def null(self):
        """
        Gets the null of this JsonNode.

        :return: The null of this JsonNode.
        :rtype: bool
        """
        return self._null

    @null.setter
    def null(self, null):
        """
        Sets the null of this JsonNode.

        :param null: The null of this JsonNode.
        :type: bool
        """

        self._null = null

    @property
    def number(self):
        """
        Gets the number of this JsonNode.

        :return: The number of this JsonNode.
        :rtype: bool
        """
        return self._number

    @number.setter
    def number(self, number):
        """
        Sets the number of this JsonNode.

        :param number: The number of this JsonNode.
        :type: bool
        """

        self._number = number

    @property
    def object(self):
        """
        Gets the object of this JsonNode.

        :return: The object of this JsonNode.
        :rtype: bool
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this JsonNode.

        :param object: The object of this JsonNode.
        :type: bool
        """

        self._object = object

    @property
    def pojo(self):
        """
        Gets the pojo of this JsonNode.

        :return: The pojo of this JsonNode.
        :rtype: bool
        """
        return self._pojo

    @pojo.setter
    def pojo(self, pojo):
        """
        Sets the pojo of this JsonNode.

        :param pojo: The pojo of this JsonNode.
        :type: bool
        """

        self._pojo = pojo

    @property
    def short(self):
        """
        Gets the short of this JsonNode.

        :return: The short of this JsonNode.
        :rtype: bool
        """
        return self._short

    @short.setter
    def short(self, short):
        """
        Sets the short of this JsonNode.

        :param short: The short of this JsonNode.
        :type: bool
        """

        self._short = short

    @property
    def textual(self):
        """
        Gets the textual of this JsonNode.

        :return: The textual of this JsonNode.
        :rtype: bool
        """
        return self._textual

    @textual.setter
    def textual(self, textual):
        """
        Sets the textual of this JsonNode.

        :param textual: The textual of this JsonNode.
        :type: bool
        """

        self._textual = textual

    @property
    def value_node(self):
        """
        Gets the value_node of this JsonNode.

        :return: The value_node of this JsonNode.
        :rtype: bool
        """
        return self._value_node

    @value_node.setter
    def value_node(self, value_node):
        """
        Sets the value_node of this JsonNode.

        :param value_node: The value_node of this JsonNode.
        :type: bool
        """

        self._value_node = value_node

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
        if not isinstance(other, JsonNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
