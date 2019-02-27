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


class ClassifierModel(object):
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
        'checkpoint_file_resource_id': 'str',
        'creation_end_time': 'int',
        'creation_start_time': 'int',
        'config': 'dict(str, str)',
        'description': 'str',
        'id': 'str',
        'initialized_time': 'int',
        'l1_regularization_strength': 'float',
        'l2_regularization_strength': 'float',
        'learning_rate': 'float',
        'metadata': 'object',
        'model_file_resource_id': 'str',
        'name': 'str',
        'prob_threshold': 'float',
        'resource_set_id': 'str',
        'state': 'str',
        'tags': 'dict(str, object)',
        'test_eval_result_file_resource_id': 'str',
        'training_history': 'list[ValidationMetrics]',
        'validation_eval_result_file_resource_id': 'str',
        'deployable_file_resources': 'list[str]'
    }

    attribute_map = {
        'checkpoint_file_resource_id': 'checkpointFileResourceId',
        'creation_end_time': 'creationEndTime',
        'creation_start_time': 'creationStartTime',
        'config': 'config',
        'description': 'description',
        'id': 'id',
        'initialized_time': 'initializedTime',
        'l1_regularization_strength': 'l1RegularizationStrength',
        'l2_regularization_strength': 'l2RegularizationStrength',
        'learning_rate': 'learningRate',
        'metadata': 'metadata',
        'model_file_resource_id': 'modelFileResourceId',
        'name': 'name',
        'prob_threshold': 'probThreshold',
        'resource_set_id': 'resourceSetId',
        'state': 'state',
        'tags': 'tags',
        'test_eval_result_file_resource_id': 'testEvalResultFileResourceId',
        'training_history': 'trainingHistory',
        'validation_eval_result_file_resource_id': 'validationEvalResultFileResourceId',
        'deployable_file_resources': 'deployableFileResources'
    }

    def __init__(self, checkpoint_file_resource_id=None, creation_end_time=None, creation_start_time=None, config=None, description=None, id=None, initialized_time=None, l1_regularization_strength=None, l2_regularization_strength=None, learning_rate=None, metadata=None, model_file_resource_id=None, name=None, prob_threshold=None, resource_set_id=None, state=None, tags=None, test_eval_result_file_resource_id=None, training_history=None, validation_eval_result_file_resource_id=None, deployable_file_resources=None):
        """
        ClassifierModel - a model defined in Swagger
        """

        self._checkpoint_file_resource_id = None
        self._creation_end_time = None
        self._creation_start_time = None
        self._config = None
        self._description = None
        self._id = None
        self._initialized_time = None
        self._l1_regularization_strength = None
        self._l2_regularization_strength = None
        self._learning_rate = None
        self._metadata = None
        self._model_file_resource_id = None
        self._name = None
        self._prob_threshold = None
        self._resource_set_id = None
        self._state = None
        self._tags = None
        self._test_eval_result_file_resource_id = None
        self._training_history = None
        self._validation_eval_result_file_resource_id = None
        self._deployable_file_resources = None

        if checkpoint_file_resource_id is not None:
          self.checkpoint_file_resource_id = checkpoint_file_resource_id
        if creation_end_time is not None:
          self.creation_end_time = creation_end_time
        if creation_start_time is not None:
          self.creation_start_time = creation_start_time
        if config is not None:
          self.config = config
        if description is not None:
          self.description = description
        if id is not None:
          self.id = id
        if initialized_time is not None:
          self.initialized_time = initialized_time
        if l1_regularization_strength is not None:
          self.l1_regularization_strength = l1_regularization_strength
        if l2_regularization_strength is not None:
          self.l2_regularization_strength = l2_regularization_strength
        if learning_rate is not None:
          self.learning_rate = learning_rate
        if metadata is not None:
          self.metadata = metadata
        if model_file_resource_id is not None:
          self.model_file_resource_id = model_file_resource_id
        if name is not None:
          self.name = name
        if prob_threshold is not None:
          self.prob_threshold = prob_threshold
        if resource_set_id is not None:
          self.resource_set_id = resource_set_id
        if state is not None:
          self.state = state
        if tags is not None:
          self.tags = tags
        if test_eval_result_file_resource_id is not None:
          self.test_eval_result_file_resource_id = test_eval_result_file_resource_id
        if training_history is not None:
          self.training_history = training_history
        if validation_eval_result_file_resource_id is not None:
          self.validation_eval_result_file_resource_id = validation_eval_result_file_resource_id
        if deployable_file_resources is not None:
          self.deployable_file_resources = deployable_file_resources

    @property
    def checkpoint_file_resource_id(self):
        """
        Gets the checkpoint_file_resource_id of this ClassifierModel.
        (Used by system)

        :return: The checkpoint_file_resource_id of this ClassifierModel.
        :rtype: str
        """
        return self._checkpoint_file_resource_id

    @checkpoint_file_resource_id.setter
    def checkpoint_file_resource_id(self, checkpoint_file_resource_id):
        """
        Sets the checkpoint_file_resource_id of this ClassifierModel.
        (Used by system)

        :param checkpoint_file_resource_id: The checkpoint_file_resource_id of this ClassifierModel.
        :type: str
        """

        self._checkpoint_file_resource_id = checkpoint_file_resource_id

    @property
    def creation_end_time(self):
        """
        Gets the creation_end_time of this ClassifierModel.
        Timestamp when the model creation ends

        :return: The creation_end_time of this ClassifierModel.
        :rtype: int
        """
        return self._creation_end_time

    @creation_end_time.setter
    def creation_end_time(self, creation_end_time):
        """
        Sets the creation_end_time of this ClassifierModel.
        Timestamp when the model creation ends

        :param creation_end_time: The creation_end_time of this ClassifierModel.
        :type: int
        """

        self._creation_end_time = creation_end_time

    @property
    def creation_start_time(self):
        """
        Gets the creation_start_time of this ClassifierModel.
        Timestamp when the model creation starts

        :return: The creation_start_time of this ClassifierModel.
        :rtype: int
        """
        return self._creation_start_time

    @creation_start_time.setter
    def creation_start_time(self, creation_start_time):
        """
        Sets the creation_start_time of this ClassifierModel.
        Timestamp when the model creation starts

        :param creation_start_time: The creation_start_time of this ClassifierModel.
        :type: int
        """

        self._creation_start_time = creation_start_time

    @property
    def config(self):
        """
        Gets the config of this ClassifierModel.
        Map of properties that can be passed to training process as arguments

        :return: The config of this ClassifierModel.
        :rtype: dict(str, str)
        """
        return self._config

    @config.setter
    def config(self, config):
        """
        Sets the config of this ClassifierModel.
        Map of properties that can be passed to training process as arguments

        :param config: The config of this ClassifierModel.
        :type: dict(str, str)
        """

        self._config = config

    @property
    def description(self):
        """
        Gets the description of this ClassifierModel.
        User-provided description

        :return: The description of this ClassifierModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ClassifierModel.
        User-provided description

        :param description: The description of this ClassifierModel.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this ClassifierModel.
        ID

        :return: The id of this ClassifierModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ClassifierModel.
        ID

        :param id: The id of this ClassifierModel.
        :type: str
        """

        self._id = id

    @property
    def initialized_time(self):
        """
        Gets the initialized_time of this ClassifierModel.
        Timestamp when the model is initialized

        :return: The initialized_time of this ClassifierModel.
        :rtype: int
        """
        return self._initialized_time

    @initialized_time.setter
    def initialized_time(self, initialized_time):
        """
        Sets the initialized_time of this ClassifierModel.
        Timestamp when the model is initialized

        :param initialized_time: The initialized_time of this ClassifierModel.
        :type: int
        """

        self._initialized_time = initialized_time

    @property
    def l1_regularization_strength(self):
        """
        Gets the l1_regularization_strength of this ClassifierModel.
        L1 regularization strength

        :return: The l1_regularization_strength of this ClassifierModel.
        :rtype: float
        """
        return self._l1_regularization_strength

    @l1_regularization_strength.setter
    def l1_regularization_strength(self, l1_regularization_strength):
        """
        Sets the l1_regularization_strength of this ClassifierModel.
        L1 regularization strength

        :param l1_regularization_strength: The l1_regularization_strength of this ClassifierModel.
        :type: float
        """

        self._l1_regularization_strength = l1_regularization_strength

    @property
    def l2_regularization_strength(self):
        """
        Gets the l2_regularization_strength of this ClassifierModel.
        L2 regularization strength

        :return: The l2_regularization_strength of this ClassifierModel.
        :rtype: float
        """
        return self._l2_regularization_strength

    @l2_regularization_strength.setter
    def l2_regularization_strength(self, l2_regularization_strength):
        """
        Sets the l2_regularization_strength of this ClassifierModel.
        L2 regularization strength

        :param l2_regularization_strength: The l2_regularization_strength of this ClassifierModel.
        :type: float
        """

        self._l2_regularization_strength = l2_regularization_strength

    @property
    def learning_rate(self):
        """
        Gets the learning_rate of this ClassifierModel.
        Learning rate

        :return: The learning_rate of this ClassifierModel.
        :rtype: float
        """
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, learning_rate):
        """
        Sets the learning_rate of this ClassifierModel.
        Learning rate

        :param learning_rate: The learning_rate of this ClassifierModel.
        :type: float
        """

        self._learning_rate = learning_rate

    @property
    def metadata(self):
        """
        Gets the metadata of this ClassifierModel.
        (Used by system)

        :return: The metadata of this ClassifierModel.
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this ClassifierModel.
        (Used by system)

        :param metadata: The metadata of this ClassifierModel.
        :type: object
        """

        self._metadata = metadata

    @property
    def model_file_resource_id(self):
        """
        Gets the model_file_resource_id of this ClassifierModel.
        (Used by system)

        :return: The model_file_resource_id of this ClassifierModel.
        :rtype: str
        """
        return self._model_file_resource_id

    @model_file_resource_id.setter
    def model_file_resource_id(self, model_file_resource_id):
        """
        Sets the model_file_resource_id of this ClassifierModel.
        (Used by system)

        :param model_file_resource_id: The model_file_resource_id of this ClassifierModel.
        :type: str
        """

        self._model_file_resource_id = model_file_resource_id

    @property
    def name(self):
        """
        Gets the name of this ClassifierModel.
        Name

        :return: The name of this ClassifierModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClassifierModel.
        Name

        :param name: The name of this ClassifierModel.
        :type: str
        """

        self._name = name

    @property
    def prob_threshold(self):
        """
        Gets the prob_threshold of this ClassifierModel.
        Threshold of probabilities to output predicted labels

        :return: The prob_threshold of this ClassifierModel.
        :rtype: float
        """
        return self._prob_threshold

    @prob_threshold.setter
    def prob_threshold(self, prob_threshold):
        """
        Sets the prob_threshold of this ClassifierModel.
        Threshold of probabilities to output predicted labels

        :param prob_threshold: The prob_threshold of this ClassifierModel.
        :type: float
        """

        self._prob_threshold = prob_threshold

    @property
    def resource_set_id(self):
        """
        Gets the resource_set_id of this ClassifierModel.
        ID of the resource set used to train this model

        :return: The resource_set_id of this ClassifierModel.
        :rtype: str
        """
        return self._resource_set_id

    @resource_set_id.setter
    def resource_set_id(self, resource_set_id):
        """
        Sets the resource_set_id of this ClassifierModel.
        ID of the resource set used to train this model

        :param resource_set_id: The resource_set_id of this ClassifierModel.
        :type: str
        """

        self._resource_set_id = resource_set_id

    @property
    def state(self):
        """
        Gets the state of this ClassifierModel.
        Current state of this model

        :return: The state of this ClassifierModel.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this ClassifierModel.
        Current state of this model

        :param state: The state of this ClassifierModel.
        :type: str
        """
        allowed_values = ["INITIAL", "CREATING_DATASETS", "FAILED_TO_CREATE_DATASETS", "CREATING_RESOURCES", "FAILED_TO_CREATE_RESOURCES", "TRAINING", "FAILED_TO_TRAIN", "EVALUATING", "FAILED_TO_EVALUATE", "READY_TO_DEPLOY"]
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def tags(self):
        """
        Gets the tags of this ClassifierModel.
        (Used by system)

        :return: The tags of this ClassifierModel.
        :rtype: dict(str, object)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ClassifierModel.
        (Used by system)

        :param tags: The tags of this ClassifierModel.
        :type: dict(str, object)
        """

        self._tags = tags

    @property
    def test_eval_result_file_resource_id(self):
        """
        Gets the test_eval_result_file_resource_id of this ClassifierModel.
        (Used by system)

        :return: The test_eval_result_file_resource_id of this ClassifierModel.
        :rtype: str
        """
        return self._test_eval_result_file_resource_id

    @test_eval_result_file_resource_id.setter
    def test_eval_result_file_resource_id(self, test_eval_result_file_resource_id):
        """
        Sets the test_eval_result_file_resource_id of this ClassifierModel.
        (Used by system)

        :param test_eval_result_file_resource_id: The test_eval_result_file_resource_id of this ClassifierModel.
        :type: str
        """

        self._test_eval_result_file_resource_id = test_eval_result_file_resource_id

    @property
    def training_history(self):
        """
        Gets the training_history of this ClassifierModel.
        History of loss values during the training

        :return: The training_history of this ClassifierModel.
        :rtype: list[ValidationMetrics]
        """
        return self._training_history

    @training_history.setter
    def training_history(self, training_history):
        """
        Sets the training_history of this ClassifierModel.
        History of loss values during the training

        :param training_history: The training_history of this ClassifierModel.
        :type: list[ValidationMetrics]
        """

        self._training_history = training_history

    @property
    def validation_eval_result_file_resource_id(self):
        """
        Gets the validation_eval_result_file_resource_id of this ClassifierModel.
        (Used by system)

        :return: The validation_eval_result_file_resource_id of this ClassifierModel.
        :rtype: str
        """
        return self._validation_eval_result_file_resource_id

    @validation_eval_result_file_resource_id.setter
    def validation_eval_result_file_resource_id(self, validation_eval_result_file_resource_id):
        """
        Sets the validation_eval_result_file_resource_id of this ClassifierModel.
        (Used by system)

        :param validation_eval_result_file_resource_id: The validation_eval_result_file_resource_id of this ClassifierModel.
        :type: str
        """

        self._validation_eval_result_file_resource_id = validation_eval_result_file_resource_id

    @property
    def deployable_file_resources(self):
        """
        Gets the deployable_file_resources of this ClassifierModel.
        (Used by system)

        :return: The deployable_file_resources of this ClassifierModel.
        :rtype: list[str]
        """
        return self._deployable_file_resources

    @deployable_file_resources.setter
    def deployable_file_resources(self, deployable_file_resources):
        """
        Sets the deployable_file_resources of this ClassifierModel.
        (Used by system)

        :param deployable_file_resources: The deployable_file_resources of this ClassifierModel.
        :type: list[str]
        """

        self._deployable_file_resources = deployable_file_resources

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
        if not isinstance(other, ClassifierModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
