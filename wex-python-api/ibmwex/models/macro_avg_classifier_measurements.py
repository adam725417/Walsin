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


class MacroAvgClassifierMeasurements(object):
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
        'f1': 'float',
        'precision': 'float',
        'recall': 'float'
    }

    attribute_map = {
        'f1': 'f1',
        'precision': 'precision',
        'recall': 'recall'
    }

    def __init__(self, f1=None, precision=None, recall=None):
        """
        MacroAvgClassifierMeasurements - a model defined in Swagger
        """

        self._f1 = None
        self._precision = None
        self._recall = None

        if f1 is not None:
          self.f1 = f1
        if precision is not None:
          self.precision = precision
        if recall is not None:
          self.recall = recall

    @property
    def f1(self):
        """
        Gets the f1 of this MacroAvgClassifierMeasurements.
        F1-score

        :return: The f1 of this MacroAvgClassifierMeasurements.
        :rtype: float
        """
        return self._f1

    @f1.setter
    def f1(self, f1):
        """
        Sets the f1 of this MacroAvgClassifierMeasurements.
        F1-score

        :param f1: The f1 of this MacroAvgClassifierMeasurements.
        :type: float
        """

        self._f1 = f1

    @property
    def precision(self):
        """
        Gets the precision of this MacroAvgClassifierMeasurements.
        Precision

        :return: The precision of this MacroAvgClassifierMeasurements.
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """
        Sets the precision of this MacroAvgClassifierMeasurements.
        Precision

        :param precision: The precision of this MacroAvgClassifierMeasurements.
        :type: float
        """

        self._precision = precision

    @property
    def recall(self):
        """
        Gets the recall of this MacroAvgClassifierMeasurements.
        Recall

        :return: The recall of this MacroAvgClassifierMeasurements.
        :rtype: float
        """
        return self._recall

    @recall.setter
    def recall(self, recall):
        """
        Sets the recall of this MacroAvgClassifierMeasurements.
        Recall

        :param recall: The recall of this MacroAvgClassifierMeasurements.
        :type: float
        """

        self._recall = recall

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
        if not isinstance(other, MacroAvgClassifierMeasurements):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
