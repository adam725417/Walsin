# ibmwex.GroupApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupApi.md#create_group) | **POST** /api/v1/usermgmt/groups | Create group
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /api/v1/usermgmt/groups/{name} | Remove group
[**get_group**](GroupApi.md#get_group) | **GET** /api/v1/usermgmt/groups/{name} | Get group
[**list_groups**](GroupApi.md#list_groups) | **GET** /api/v1/usermgmt/groups | List groups
[**list_user_in_group**](GroupApi.md#list_user_in_group) | **GET** /api/v1/usermgmt/groups/{name}/users | List users in a group
[**update_group**](GroupApi.md#update_group) | **PUT** /api/v1/usermgmt/groups/{name} | Update group


# **create_group**
> UserGroup create_group(body)

Create group

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
api_instance = ibmwex.GroupApi()
body = ibmwex.UserGroup() # UserGroup | Create user object

try: 
    # Create group
    api_response = api_instance.create_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserGroup**](UserGroup.md)| Create user object | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(name, force=force)

Remove group

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
api_instance = ibmwex.GroupApi()
name = 'name_example' # str | The name that needs to be deleted
force = true # bool | Remove group from users and remove the group. (optional)

try: 
    # Remove group
    api_instance.delete_group(name, force=force)
except ApiException as e:
    print("Exception when calling GroupApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name that needs to be deleted | 
 **force** | **bool**| Remove group from users and remove the group. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> UserGroup get_group(name)

Get group

Get group info

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
api_instance = ibmwex.GroupApi()
name = 'name_example' # str | The name that needs to be fetched

try: 
    # Get group
    api_response = api_instance.get_group(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name that needs to be fetched | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> list[UserGroup] list_groups()

List groups

List all groups

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
api_instance = ibmwex.GroupApi()

try: 
    # List groups
    api_response = api_instance.list_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UserGroup]**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_in_group**
> list[str] list_user_in_group(name, offset=offset, size=size)

List users in a group

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
api_instance = ibmwex.GroupApi()
name = 'name_example' # str | The name that needs to be fetched
offset = 56 # int | Offset of the users returned (optional)
size = 56 # int | Number of users returned (optional)

try: 
    # List users in a group
    api_response = api_instance.list_user_in_group(name, offset=offset, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_user_in_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name that needs to be fetched | 
 **offset** | **int**| Offset of the users returned | [optional] 
 **size** | **int**| Number of users returned | [optional] 

### Return type

**list[str]**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> UserGroup update_group(name, body)

Update group

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
api_instance = ibmwex.GroupApi()
name = 'name_example' # str | The name that needs to be updated
body = ibmwex.UserGroup() # UserGroup | Create user object

try: 
    # Update group
    api_response = api_instance.update_group(name, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name that needs to be updated | 
 **body** | [**UserGroup**](UserGroup.md)| Create user object | 

### Return type

[**UserGroup**](UserGroup.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

