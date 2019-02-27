# ibmwex.UserApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_my_password**](UserApi.md#change_my_password) | **POST** /api/v1/usermgmt/user/changemypassword | Helps the user change his password
[**change_user_password**](UserApi.md#change_user_password) | **POST** /api/v1/usermgmt/user/changeuserpassword | Helps the admin change user&#39;s password
[**create_user**](UserApi.md#create_user) | **POST** /api/v1/usermgmt/user | Create user (or Grant Access if an External LDAP is present 
[**delete_config_file**](UserApi.md#delete_config_file) | **DELETE** /api/v1/usermgmt/config/file/{name} | Delete config file
[**delete_user**](UserApi.md#delete_user) | **DELETE** /api/v1/usermgmt/user/{username} | Delete user
[**do_logout**](UserApi.md#do_logout) | **GET** /api/v1/usermgmt/logout | Logs out current logged in user from session
[**get_admin_patterms**](UserApi.md#get_admin_patterms) | **GET** /api/v1/usermgmt/config/admin | Get list of pattern texts to make user as Admin
[**get_config_file**](UserApi.md#get_config_file) | **GET** /api/v1/usermgmt/config/file/{name} | Get config file
[**get_current_user_info**](UserApi.md#get_current_user_info) | **GET** /api/v1/usermgmt/user/currentUserInfo | Get current user info
[**get_user_by_name**](UserApi.md#get_user_by_name) | **GET** /api/v1/usermgmt/user/{username} | Get user details by user name
[**list_config_file**](UserApi.md#list_config_file) | **GET** /api/v1/usermgmt/config/file/ | List config files
[**list_users**](UserApi.md#list_users) | **GET** /api/v1/usermgmt/users | Get all users
[**put_admin_patterns**](UserApi.md#put_admin_patterns) | **POST** /api/v1/usermgmt/config/admin | Put list of pattern texts to make user as Admin
[**signin_user**](UserApi.md#signin_user) | **POST** /api/v1/usermgmt/login | Logs user into the system
[**update_user**](UserApi.md#update_user) | **PUT** /api/v1/usermgmt/user/{username} | Update user record (including his password/hash)
[**upload_config_file**](UserApi.md#upload_config_file) | **POST** /api/v1/usermgmt/config/file/{name} | Upload config file
[**user_sign_up**](UserApi.md#user_sign_up) | **POST** /api/v1/usermgmt/signup | User requesting access
[**validate_user**](UserApi.md#validate_user) | **GET** /api/v1/usermgmt/validate | Almost an alias to the signin method. but intended for REST APIs


# **change_my_password**
> change_my_password(password)

Helps the user change his password

Only if external LDAP is not setup

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
password = 'password_example' # str | The new password for the currently logged in user

try: 
    # Helps the user change his password
    api_instance.change_my_password(password)
except ApiException as e:
    print("Exception when calling UserApi->change_my_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **str**| The new password for the currently logged in user | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_password**
> change_user_password(username, password)

Helps the admin change user's password

Only if external LDAP is not setup

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | The username for user that needs new password
password = 'password_example' # str | The new password for the currently logged in user

try: 
    # Helps the admin change user's password
    api_instance.change_user_password(username, password)
except ApiException as e:
    print("Exception when calling UserApi->change_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The username for user that needs new password | 
 **password** | **str**| The new password for the currently logged in user | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> create_user(body)

Create user (or Grant Access if an External LDAP is present 

This can only be done by a user with an admin role. The admin would provide the user's details and if LDAP is setup, also select if the user is to be authenticated by LDAP or by our internal repo. If External LDAP is picked as an authenticator for the user, password should not be prompted for - since the Admin will not have the user's password. Else, if the internal authenticator is used, the password would be an initial default - which the user can change after they login. 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
body = ibmwex.User() # User | Create user object

try: 
    # Create user (or Grant Access if an External LDAP is present 
    api_instance.create_user(body)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**User**](User.md)| Create user object | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config_file**
> delete_config_file(name)

Delete config file

_**Needs Admin role**_ Delete config file 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
name = 'name_example' # str | File name

try: 
    # Delete config file
    api_instance.delete_config_file(name)
except ApiException as e:
    print("Exception when calling UserApi->delete_config_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| File name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(username)

Delete user

This can only be done by an admin. Note the initial 'admin' user cannot be deleted

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | The name that needs to be deleted

try: 
    # Delete user
    api_instance.delete_user(username)
except ApiException as e:
    print("Exception when calling UserApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be deleted | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_logout**
> do_logout()

Logs out current logged in user from session

should only be shown when the user is logged in. The generated JWT token should be deleted from the repo as well. 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()

try: 
    # Logs out current logged in user from session
    api_instance.do_logout()
except ApiException as e:
    print("Exception when calling UserApi->do_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_admin_patterms**
> list[GroupPattern] get_admin_patterms()

Get list of pattern texts to make user as Admin

_**Needs Admin role**_ Get list of pattern texts to make user as Admin. See [POST /api/v1/usermgmt/config/admin](#!/User/putAdminPatterns) 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()

try: 
    # Get list of pattern texts to make user as Admin
    api_response = api_instance.get_admin_patterms()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_admin_patterms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[GroupPattern]**](GroupPattern.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_config_file**
> get_config_file(name)

Get config file

_**Needs Admin role**_ Get content of a config file 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
name = 'name_example' # str | File name

try: 
    # Get config file
    api_instance.get_config_file(name)
except ApiException as e:
    print("Exception when calling UserApi->get_config_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| File name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_info**
> User get_current_user_info()

Get current user info

Get current user info. No sensitive info - not even the password hash

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()

try: 
    # Get current user info
    api_response = api_instance.get_current_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_current_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_name**
> User get_user_by_name(username)

Get user details by user name

If admin, then can retrieve any user info. Otherwise, only current user's info.  In any case, no sensitive info - not even the password hash

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | The name that needs to be fetched

try: 
    # Get user details by user name
    api_response = api_instance.get_user_by_name(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The name that needs to be fetched | 

### Return type

[**User**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_config_file**
> list[ConfigFile] list_config_file()

List config files

_**Needs Admin role**_ List config files 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()

try: 
    # List config files
    api_response = api_instance.list_config_file()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_config_file: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ConfigFile]**](ConfigFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> list[User] list_users(include_all=include_all)

Get all users

Gets `User` objects. Optional query param of **includeAll** determines whether to include user entries that are in pending or  denied state else only access-granted users will be returned.  _**Needs Admin role**_ no sensitive info - not even the password hash returned 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
include_all = true # bool | set to true to include users in pending/denied access states too (optional)

try: 
    # Get all users
    api_response = api_instance.list_users(include_all=include_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_all** | **bool**| set to true to include users in pending/denied access states too | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_admin_patterns**
> put_admin_patterns(body=body)

Put list of pattern texts to make user as Admin

_**Needs Admin role**_ Set list of pattern texts to make user as Admin. For each patterns, each user and groups are evaluated. Once pattern matches, user will be Admin (allow=true) or User(allow=false). If not of pattern matches any of user's group, user's role is set as \"User\" 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
body = [ibmwex.GroupPattern()] # list[GroupPattern] |  (optional)

try: 
    # Put list of pattern texts to make user as Admin
    api_instance.put_admin_patterns(body=body)
except ApiException as e:
    print("Exception when calling UserApi->put_admin_patterns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[GroupPattern]**](GroupPattern.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signin_user**
> str signin_user(username, password)

Logs user into the system

This option should only be shown if the user is not already logged in.  If external LDAP is used as the authenticator for this user record , the login method will delegate the username/password validation to that ldap host. Else it would generate the 1-way hash using the supplied password and compare it with the hash stored in the repo for that user.  As part of the login flow, a JWT token will be generated with the username, role, a refresh_timestamp in the payload. This would also be stored in the cloudant repo. It will also be set as a cookie to keep track of the user's session.  The refresh_timestamp will be used later on to verify if the user's record is still current & if so, regenerate the JWT token. This cycle repeats at regular intervals on user http requests. If the user is idle or has closed off his browser - the cookie will become invalid since the refresh timestamp would have expired & the customer would need to re-sign in.   Once sign in is complete, if the request is complete, the user's browser is redirected to the URL that they were in previously before being redirected to sign in page.   Sign-in Variation: We should also support the standard Basic Auth for REST API. The user can provide a Authorization: Basic base64-ed header when requesting a target URL.We would need to seamlessly validate their Basic Auth credentials and continue their request to their target URL. Note: We cannot throw a 302 redirect like we would to the browser.  To this end, we would have an internal REST function (say /user/validateAuth) that is invoked by the nginx proxy when it encounters the Basic Auth header to validate the credentials. This function would return the JWT token and a 200 for success. On failure, returns a 401 with error messages just like /user/signin.  The nginx proxy, on success, would proxy_pass the request to the requested target URL.   Lockout Policy: (v2 Candidate) If the number of login attempts (recent_number_of_failed_attempts) exceed 'policy_numfailedattempts' within the last 'policy_numfailedattempts_timeperiod' minutes, then lock the user account for 30 minutes. If after that time, the user tries again, the lock is released 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | The user name for login
password = 'password_example' # str | The password for login in clear text

try: 
    # Logs user into the system
    api_response = api_instance.signin_user(username, password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->signin_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user name for login | 
 **password** | **str**| The password for login in clear text | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(username, body)

Update user record (including his password/hash)

This can only be done by an admin

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | name that need to be updated
body = ibmwex.User() # User | Updated user object

try: 
    # Update user record (including his password/hash)
    api_instance.update_user(username, body)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| name that need to be updated | 
 **body** | [**User**](User.md)| Updated user object | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_config_file**
> ConfigFile upload_config_file(name, no_encode=no_encode, content=content)

Upload config file

_**Needs Admin role**_ Upload single configuratil file to the server. Attributes \"password\", \"bindPassword\" and \"keysPassword\" will be encoded by aes if XML file under 1MB. 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
ibmwex.configuration.username = 'YOUR_USERNAME'
ibmwex.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = ibmwex.UserApi()
name = 'name_example' # str | File name
no_encode = true # bool | true to disable encode passwords (optional)
content = 'B' # str | Content of a file (optional)

try: 
    # Upload config file
    api_response = api_instance.upload_config_file(name, no_encode=no_encode, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->upload_config_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| File name | 
 **no_encode** | **bool**| true to disable encode passwords | [optional] 
 **content** | **str**| Content of a file | [optional] 

### Return type

[**ConfigFile**](ConfigFile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_sign_up**
> user_sign_up(username, display_name, email=email, password=password, approval_status=approval_status, authenticator=authenticator)

User requesting access

This option should only be shown if the user is not already logged in. The use provides their username and password.  We first validate if they have already signed up and if so - we show whether their status is pending/denied/approved etc.  If its ExternalLDAP - then we would validate that their entry exists in LDAP, by doing an ldap bind with their creds.  The user record is stored with 'approval_status' set to 'pending', for an admin to approve.  The config setting 'auto_signup' that automatically approves all signups.  If the Admin has setup an External LDAP - all signups will assume that the username is an LDAP user. (Workaround - if somebody really want an internal username, the Admin will add for them or change their record from internal to external). (or) An alternative -there is a checkbox that says \"Authenticate against LDAP\" -this is checked on by  default.  If the user unchecks this, then the user gets created in the \"internal\" repo.  The new user cannot request an 'admin' role - but can only be granted the Admin privilege by another admin.  Password is not to be prompted for .   Candidate for v2 ? - workaround is an Admin adds every user to our User list. 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | The user name for login
display_name = 'display_name_example' # str | The display name of user when logged in.
email = 'email_example' # str | The email of user when logged in. (optional)
password = 'password_example' # str | The password for login in clear text (optional)
approval_status = 'approval_status_example' # str | If LDAP is set up with auto-signup, set this to \"enabled\" (optional)
authenticator = 'authenticator_example' # str | The authenticator for login in clear text (optional)

try: 
    # User requesting access
    api_instance.user_sign_up(username, display_name, email=email, password=password, approval_status=approval_status, authenticator=authenticator)
except ApiException as e:
    print("Exception when calling UserApi->user_sign_up: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user name for login | 
 **display_name** | **str**| The display name of user when logged in. | 
 **email** | **str**| The email of user when logged in. | [optional] 
 **password** | **str**| The password for login in clear text | [optional] 
 **approval_status** | **str**| If LDAP is set up with auto-signup, set this to \&quot;enabled\&quot; | [optional] 
 **authenticator** | **str**| The authenticator for login in clear text | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_user**
> str validate_user(username=username, password=password, authorization=authorization)

Almost an alias to the signin method. but intended for REST APIs

For clients that cannot tolerate cookies or redirects and would prefer to use Basic auth headers or Bearer tokens instead. Intended to be invoked by our nginx proxy to seamlessly pass through the request to the right target url.  send out Authorization: Basic <base64ed username:password>  OR Authorization: Bearer <token> 

### Example 
```python
from __future__ import print_function
import time
import ibmwex
from ibmwex.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ibmwex.UserApi()
username = 'username_example' # str | The user name part in Basic Auth (optional)
password = 'password_example' # str | The password part in Basic Auth (optional)
authorization = 'authorization_example' # str | The bearer token part in Bearer Auth.  (optional)

try: 
    # Almost an alias to the signin method. but intended for REST APIs
    api_response = api_instance.validate_user(username=username, password=password, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->validate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| The user name part in Basic Auth | [optional] 
 **password** | **str**| The password part in Basic Auth | [optional] 
 **authorization** | **str**| The bearer token part in Bearer Auth.  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

