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


class User(object):
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
        'username': 'str',
        'authenticator': 'str',
        'password': 'str',
        'salt': 'str',
        'password_hash': 'str',
        'role': 'str',
        'email': 'str',
        'default_user': 'str',
        'created_timestamp': 'float',
        'last_modified_timestamp': 'float',
        'approval_status': 'str',
        'current_account_status': 'str',
        'release_lock_at_timestamp': 'float',
        'first_failed_attempt_timestamp': 'float',
        'recent_number_of_failed_attempts': 'float',
        'default_auth_jwt_token': 'str',
        'groups': 'list[str]'
    }

    attribute_map = {
        'username': 'username',
        'authenticator': 'authenticator',
        'password': 'password',
        'salt': 'salt',
        'password_hash': 'password_hash',
        'role': 'role',
        'email': 'email',
        'default_user': 'default_user',
        'created_timestamp': 'created_timestamp',
        'last_modified_timestamp': 'last_modified_timestamp',
        'approval_status': 'approval_status',
        'current_account_status': 'current_account_status',
        'release_lock_at_timestamp': 'release_lock_at_timestamp',
        'first_failed_attempt_timestamp': 'first_failed_attempt_timestamp',
        'recent_number_of_failed_attempts': 'recent_number_of_failed_attempts',
        'default_auth_jwt_token': 'default_auth_jwt_token',
        'groups': 'groups'
    }

    def __init__(self, username=None, authenticator=None, password=None, salt=None, password_hash=None, role=None, email=None, default_user=None, created_timestamp=None, last_modified_timestamp=None, approval_status=None, current_account_status=None, release_lock_at_timestamp=None, first_failed_attempt_timestamp=None, recent_number_of_failed_attempts=None, default_auth_jwt_token=None, groups=None):
        """
        User - a model defined in Swagger
        """

        self._username = None
        self._authenticator = None
        self._password = None
        self._salt = None
        self._password_hash = None
        self._role = None
        self._email = None
        self._default_user = None
        self._created_timestamp = None
        self._last_modified_timestamp = None
        self._approval_status = None
        self._current_account_status = None
        self._release_lock_at_timestamp = None
        self._first_failed_attempt_timestamp = None
        self._recent_number_of_failed_attempts = None
        self._default_auth_jwt_token = None
        self._groups = None

        self.username = username
        if authenticator is not None:
          self.authenticator = authenticator
        if password is not None:
          self.password = password
        if salt is not None:
          self.salt = salt
        if password_hash is not None:
          self.password_hash = password_hash
        if role is not None:
          self.role = role
        if email is not None:
          self.email = email
        if default_user is not None:
          self.default_user = default_user
        if created_timestamp is not None:
          self.created_timestamp = created_timestamp
        if last_modified_timestamp is not None:
          self.last_modified_timestamp = last_modified_timestamp
        if approval_status is not None:
          self.approval_status = approval_status
        if current_account_status is not None:
          self.current_account_status = current_account_status
        if release_lock_at_timestamp is not None:
          self.release_lock_at_timestamp = release_lock_at_timestamp
        if first_failed_attempt_timestamp is not None:
          self.first_failed_attempt_timestamp = first_failed_attempt_timestamp
        if recent_number_of_failed_attempts is not None:
          self.recent_number_of_failed_attempts = recent_number_of_failed_attempts
        if default_auth_jwt_token is not None:
          self.default_auth_jwt_token = default_auth_jwt_token
        if groups is not None:
          self.groups = groups

    @property
    def username(self):
        """
        Gets the username of this User.
        if \"authenicator\" is external LDAP note that the username needs to be present in the external LDAP server and should be checked during the \"signUp\" function implementation, by prompting the user to enter their LDAP password (which should not be signed).

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.
        if \"authenicator\" is external LDAP note that the username needs to be present in the external LDAP server and should be checked during the \"signUp\" function implementation, by prompting the user to enter their LDAP password (which should not be signed).

        :param username: The username of this User.
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")

        self._username = username

    @property
    def authenticator(self):
        """
        Gets the authenticator of this User.
        when an external LDAP is hooked up, this option can be used to decide how to login the user. If external LDAP - then the username/password can be supplied to that ldap server to validate, else validated by our own internal 1-way hash.  When an external LDAP is setup,  Sign-ups can only be external LDAP usernames.  The internal mechanism can be used by Admins to add individual users not present in their LDAP, say usernames with fixed passwords or test users or even \"functional IDS\"/service keys.

        :return: The authenticator of this User.
        :rtype: str
        """
        return self._authenticator

    @authenticator.setter
    def authenticator(self, authenticator):
        """
        Sets the authenticator of this User.
        when an external LDAP is hooked up, this option can be used to decide how to login the user. If external LDAP - then the username/password can be supplied to that ldap server to validate, else validated by our own internal 1-way hash.  When an external LDAP is setup,  Sign-ups can only be external LDAP usernames.  The internal mechanism can be used by Admins to add individual users not present in their LDAP, say usernames with fixed passwords or test users or even \"functional IDS\"/service keys.

        :param authenticator: The authenticator of this User.
        :type: str
        """
        allowed_values = ["default", "external"]
        if authenticator not in allowed_values:
            raise ValueError(
                "Invalid value for `authenticator` ({0}), must be one of {1}"
                .format(authenticator, allowed_values)
            )

        self._authenticator = authenticator

    @property
    def password(self):
        """
        Gets the password of this User.
        transient information, not persisted in the repo. Only the hash is (and that too not if an External LDAP user)

        :return: The password of this User.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this User.
        transient information, not persisted in the repo. Only the hash is (and that too not if an External LDAP user)

        :param password: The password of this User.
        :type: str
        """

        self._password = password

    @property
    def salt(self):
        """
        Gets the salt of this User.
        random string generated and used to create the hash. The username, salt and password together would be used to generate the hash. Every password set/change for every user will result in a different salt - so even if you choose the same password, the hash will be different.

        :return: The salt of this User.
        :rtype: str
        """
        return self._salt

    @salt.setter
    def salt(self, salt):
        """
        Sets the salt of this User.
        random string generated and used to create the hash. The username, salt and password together would be used to generate the hash. Every password set/change for every user will result in a different salt - so even if you choose the same password, the hash will be different.

        :param salt: The salt of this User.
        :type: str
        """

        self._salt = salt

    @property
    def password_hash(self):
        """
        Gets the password_hash of this User.
        This is a 1-way hash. We will not even store this hash for an external LDAP user

        :return: The password_hash of this User.
        :rtype: str
        """
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password_hash):
        """
        Sets the password_hash of this User.
        This is a 1-way hash. We will not even store this hash for an external LDAP user

        :param password_hash: The password_hash of this User.
        :type: str
        """

        self._password_hash = password_hash

    @property
    def role(self):
        """
        Gets the role of this User.
        only two roles for now. The out-of-the-box user would be the first admin and non-deletable too.

        :return: The role of this User.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this User.
        only two roles for now. The out-of-the-box user would be the first admin and non-deletable too.

        :param role: The role of this User.
        :type: str
        """
        allowed_values = ["Admin", "User"]
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def email(self):
        """
        Gets the email of this User.
        might be useful for reset password etc.

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        might be useful for reset password etc.

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def default_user(self):
        """
        Gets the default_user of this User.
        not to be deleted

        :return: The default_user of this User.
        :rtype: str
        """
        return self._default_user

    @default_user.setter
    def default_user(self, default_user):
        """
        Sets the default_user of this User.
        not to be deleted

        :param default_user: The default_user of this User.
        :type: str
        """

        self._default_user = default_user

    @property
    def created_timestamp(self):
        """
        Gets the created_timestamp of this User.
        milliseconds from epoch. tracks when  this record was created

        :return: The created_timestamp of this User.
        :rtype: float
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """
        Sets the created_timestamp of this User.
        milliseconds from epoch. tracks when  this record was created

        :param created_timestamp: The created_timestamp of this User.
        :type: float
        """

        self._created_timestamp = created_timestamp

    @property
    def last_modified_timestamp(self):
        """
        Gets the last_modified_timestamp of this User.
        milliseconds from epoch. tracks when  this record was last updated

        :return: The last_modified_timestamp of this User.
        :rtype: float
        """
        return self._last_modified_timestamp

    @last_modified_timestamp.setter
    def last_modified_timestamp(self, last_modified_timestamp):
        """
        Sets the last_modified_timestamp of this User.
        milliseconds from epoch. tracks when  this record was last updated

        :param last_modified_timestamp: The last_modified_timestamp of this User.
        :type: float
        """

        self._last_modified_timestamp = last_modified_timestamp

    @property
    def approval_status(self):
        """
        Gets the approval_status of this User.
        tracks this user's sign up request status

        :return: The approval_status of this User.
        :rtype: str
        """
        return self._approval_status

    @approval_status.setter
    def approval_status(self, approval_status):
        """
        Sets the approval_status of this User.
        tracks this user's sign up request status

        :param approval_status: The approval_status of this User.
        :type: str
        """
        allowed_values = ["pending", "approved", "denied"]
        if approval_status not in allowed_values:
            raise ValueError(
                "Invalid value for `approval_status` ({0}), must be one of {1}"
                .format(approval_status, allowed_values)
            )

        self._approval_status = approval_status

    @property
    def current_account_status(self):
        """
        Gets the current_account_status of this User.
        tracks if the user has been locked out or if his account is still active

        :return: The current_account_status of this User.
        :rtype: str
        """
        return self._current_account_status

    @current_account_status.setter
    def current_account_status(self, current_account_status):
        """
        Sets the current_account_status of this User.
        tracks if the user has been locked out or if his account is still active

        :param current_account_status: The current_account_status of this User.
        :type: str
        """
        allowed_values = ["locked", "enabled"]
        if current_account_status not in allowed_values:
            raise ValueError(
                "Invalid value for `current_account_status` ({0}), must be one of {1}"
                .format(current_account_status, allowed_values)
            )

        self._current_account_status = current_account_status

    @property
    def release_lock_at_timestamp(self):
        """
        Gets the release_lock_at_timestamp of this User.
        milliseconds from epoch. Tracks when the user will be allowed to log back in. i.e.  a subsequent login attempt will cause the locked state to automatically switch to enabled if the 'penalty' time has elapsed.

        :return: The release_lock_at_timestamp of this User.
        :rtype: float
        """
        return self._release_lock_at_timestamp

    @release_lock_at_timestamp.setter
    def release_lock_at_timestamp(self, release_lock_at_timestamp):
        """
        Sets the release_lock_at_timestamp of this User.
        milliseconds from epoch. Tracks when the user will be allowed to log back in. i.e.  a subsequent login attempt will cause the locked state to automatically switch to enabled if the 'penalty' time has elapsed.

        :param release_lock_at_timestamp: The release_lock_at_timestamp of this User.
        :type: float
        """

        self._release_lock_at_timestamp = release_lock_at_timestamp

    @property
    def first_failed_attempt_timestamp(self):
        """
        Gets the first_failed_attempt_timestamp of this User.
        milliseconds from epoch

        :return: The first_failed_attempt_timestamp of this User.
        :rtype: float
        """
        return self._first_failed_attempt_timestamp

    @first_failed_attempt_timestamp.setter
    def first_failed_attempt_timestamp(self, first_failed_attempt_timestamp):
        """
        Sets the first_failed_attempt_timestamp of this User.
        milliseconds from epoch

        :param first_failed_attempt_timestamp: The first_failed_attempt_timestamp of this User.
        :type: float
        """

        self._first_failed_attempt_timestamp = first_failed_attempt_timestamp

    @property
    def recent_number_of_failed_attempts(self):
        """
        Gets the recent_number_of_failed_attempts of this User.
        represents the number of attempts the user has tried to login recently. If the user has had > 5 attempts in the last 5 minutes, the lock status would be set to 3

        :return: The recent_number_of_failed_attempts of this User.
        :rtype: float
        """
        return self._recent_number_of_failed_attempts

    @recent_number_of_failed_attempts.setter
    def recent_number_of_failed_attempts(self, recent_number_of_failed_attempts):
        """
        Sets the recent_number_of_failed_attempts of this User.
        represents the number of attempts the user has tried to login recently. If the user has had > 5 attempts in the last 5 minutes, the lock status would be set to 3

        :param recent_number_of_failed_attempts: The recent_number_of_failed_attempts of this User.
        :type: float
        """

        self._recent_number_of_failed_attempts = recent_number_of_failed_attempts

    @property
    def default_auth_jwt_token(self):
        """
        Gets the default_auth_jwt_token of this User.
        deprecated

        :return: The default_auth_jwt_token of this User.
        :rtype: str
        """
        return self._default_auth_jwt_token

    @default_auth_jwt_token.setter
    def default_auth_jwt_token(self, default_auth_jwt_token):
        """
        Sets the default_auth_jwt_token of this User.
        deprecated

        :param default_auth_jwt_token: The default_auth_jwt_token of this User.
        :type: str
        """

        self._default_auth_jwt_token = default_auth_jwt_token

    @property
    def groups(self):
        """
        Gets the groups of this User.
        List of group name user belongs to

        :return: The groups of this User.
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """
        Sets the groups of this User.
        List of group name user belongs to

        :param groups: The groups of this User.
        :type: list[str]
        """

        self._groups = groups

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other