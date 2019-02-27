# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | if \&quot;authenicator\&quot; is external LDAP note that the username needs to be present in the external LDAP server and should be checked during the \&quot;signUp\&quot; function implementation, by prompting the user to enter their LDAP password (which should not be signed). | 
**authenticator** | **str** | when an external LDAP is hooked up, this option can be used to decide how to login the user. If external LDAP - then the username/password can be supplied to that ldap server to validate, else validated by our own internal 1-way hash.  When an external LDAP is setup,  Sign-ups can only be external LDAP usernames.  The internal mechanism can be used by Admins to add individual users not present in their LDAP, say usernames with fixed passwords or test users or even \&quot;functional IDS\&quot;/service keys. | [optional] 
**password** | **str** | transient information, not persisted in the repo. Only the hash is (and that too not if an External LDAP user) | [optional] 
**salt** | **str** | random string generated and used to create the hash. The username, salt and password together would be used to generate the hash. Every password set/change for every user will result in a different salt - so even if you choose the same password, the hash will be different. | [optional] 
**password_hash** | **str** | This is a 1-way hash. We will not even store this hash for an external LDAP user | [optional] 
**role** | **str** | only two roles for now. The out-of-the-box user would be the first admin and non-deletable too. | [optional] 
**email** | **str** | might be useful for reset password etc. | [optional] 
**default_user** | **str** | not to be deleted | [optional] 
**created_timestamp** | **float** | milliseconds from epoch. tracks when  this record was created | [optional] 
**last_modified_timestamp** | **float** | milliseconds from epoch. tracks when  this record was last updated | [optional] 
**approval_status** | **str** | tracks this user&#39;s sign up request status | [optional] 
**current_account_status** | **str** | tracks if the user has been locked out or if his account is still active | [optional] 
**release_lock_at_timestamp** | **float** | milliseconds from epoch. Tracks when the user will be allowed to log back in. i.e.  a subsequent login attempt will cause the locked state to automatically switch to enabled if the &#39;penalty&#39; time has elapsed. | [optional] 
**first_failed_attempt_timestamp** | **float** | milliseconds from epoch | [optional] 
**recent_number_of_failed_attempts** | **float** | represents the number of attempts the user has tried to login recently. If the user has had &gt; 5 attempts in the last 5 minutes, the lock status would be set to 3 | [optional] 
**default_auth_jwt_token** | **str** | deprecated | [optional] 
**groups** | **list[str]** | List of group name user belongs to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


