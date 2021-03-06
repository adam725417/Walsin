# ibmwex
Authentication methods - Basic Auth - JSON Web Token   - [POST /api/v1/usermgmt/login](#!/User/signinUser)   - [POST /api/v1/usermgmt/logout](#!/User/doLogout) - Python client sample [Download](/docs/wex-python-api.zip) 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 12.0.2.417
- Package version: 12.0.2.417
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import ibmwex 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ibmwex
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = ibmwex.CollectionApi()
body = ibmwex.Collection() # Collection | 

try:
    # Create a collection
    api_response = api_instance.create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CollectionApi->create: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CollectionApi* | [**create**](docs/CollectionApi.md#create) | **POST** /api/v1/collections | Create a collection
*CollectionApi* | [**delete**](docs/CollectionApi.md#delete) | **DELETE** /api/v1/collections/{collectionId} | Delete a collection
*CollectionApi* | [**get**](docs/CollectionApi.md#get) | **GET** /api/v1/collections/{collectionId} | List collection details
*CollectionApi* | [**is_indexing_enabled**](docs/CollectionApi.md#is_indexing_enabled) | **GET** /api/v1/collections/{collectionId}/indexing | Get indexing status
*CollectionApi* | [**list**](docs/CollectionApi.md#list) | **GET** /api/v1/collections | List collections
*CollectionApi* | [**rebuild**](docs/CollectionApi.md#rebuild) | **POST** /api/v1/collections/{collectionId}/rebuild | Request rebuild index
*CollectionApi* | [**set_indexing_enabled**](docs/CollectionApi.md#set_indexing_enabled) | **PUT** /api/v1/collections/{collectionId}/indexing | Change indexing status
*CollectionApi* | [**status**](docs/CollectionApi.md#status) | **GET** /api/v1/collections/{collectionId}/status | List collection status
*CollectionApi* | [**status_all**](docs/CollectionApi.md#status_all) | **GET** /api/v1/collections/status | List status for all collections
*CollectionApi* | [**update**](docs/CollectionApi.md#update) | **PUT** /api/v1/collections/{collectionId} | Update a collection
*ConverterApi* | [**download**](docs/ConverterApi.md#download) | **GET** /api/v1/datasets/{datasetId}/testit/download | Download TestIt result
*ConverterApi* | [**execute**](docs/ConverterApi.md#execute) | **POST** /api/v1/datasets/{datasetId}/testit/execute | Execute TestIt
*ConverterApi* | [**get_configuration_template**](docs/ConverterApi.md#get_configuration_template) | **GET** /api/v1/converter/types/{converterType} | List converter configuration
*ConverterApi* | [**get_types**](docs/ConverterApi.md#get_types) | **GET** /api/v1/converter/types | List converter types
*ConverterApi* | [**upload_r**](docs/ConverterApi.md#upload_r) | **POST** /api/v1/datasets/{datasetId}/testit/upload/remote | Upload TestIt file on remote
*ConverterApi* | [**upload_s**](docs/ConverterApi.md#upload_s) | **POST** /api/v1/datasets/{datasetId}/testit/upload/server | Upload TestIt file on server
*CrawlerApi* | [**create**](docs/CrawlerApi.md#create) | **POST** /api/v1/datasets/{datasetId}/crawlers | Create a crawler
*CrawlerApi* | [**delete**](docs/CrawlerApi.md#delete) | **DELETE** /api/v1/datasets/{datasetId}/crawlers/{crawlerId} | Delete a crawler
*CrawlerApi* | [**discover_subspaces**](docs/CrawlerApi.md#discover_subspaces) | **POST** /api/v1/crawler/subspaces | Discover subspaces
*CrawlerApi* | [**get**](docs/CrawlerApi.md#get) | **GET** /api/v1/datasets/{datasetId}/crawlers/{crawlerId} | Get a crawler configuration
*CrawlerApi* | [**get_template**](docs/CrawlerApi.md#get_template) | **GET** /api/v1/crawler/types/{crawlerTypeName} | Get a crawler template for a specified cralwer type
*CrawlerApi* | [**get_types**](docs/CrawlerApi.md#get_types) | **GET** /api/v1/crawler/types | Get a list of crawler types
*CrawlerApi* | [**list**](docs/CrawlerApi.md#list) | **GET** /api/v1/datasets/{datasetId}/crawlers | Get a list of crawlers
*CrawlerApi* | [**start**](docs/CrawlerApi.md#start) | **POST** /api/v1/datasets/{datasetId}/crawlers/{crawlerId}/start | Start a crawler
*CrawlerApi* | [**status**](docs/CrawlerApi.md#status) | **GET** /api/v1/datasets/{datasetId}/crawlers/{crawlerId}/status | List crawler status
*CrawlerApi* | [**stop**](docs/CrawlerApi.md#stop) | **POST** /api/v1/datasets/{datasetId}/crawlers/{crawlerId}/stop | Stop a crawler
*CrawlerApi* | [**update**](docs/CrawlerApi.md#update) | **PUT** /api/v1/datasets/{datasetId}/crawlers/{crawlerId} | Update a crawler configuration
*DatasetApi* | [**add_document**](docs/DatasetApi.md#add_document) | **POST** /api/v1/datasets/{datasetId}/documents | Add a document
*DatasetApi* | [**create**](docs/DatasetApi.md#create) | **POST** /api/v1/datasets | Create a dataset
*DatasetApi* | [**delete**](docs/DatasetApi.md#delete) | **DELETE** /api/v1/datasets/{datasetId} | Delete a dataset
*DatasetApi* | [**delete_document**](docs/DatasetApi.md#delete_document) | **DELETE** /api/v1/datasets/{datasetId}/documents/{documentId} | Delete a document
*DatasetApi* | [**get**](docs/DatasetApi.md#get) | **GET** /api/v1/datasets/{datasetId} | List dataset details
*DatasetApi* | [**get_converter_pipeline**](docs/DatasetApi.md#get_converter_pipeline) | **GET** /api/v1/datasets/{datasetId}/converters | List converter pileline details
*DatasetApi* | [**import_csv**](docs/DatasetApi.md#import_csv) | **POST** /api/v1/datasets/{datasetId}/import | Import a CSV file
*DatasetApi* | [**list**](docs/DatasetApi.md#list) | **GET** /api/v1/datasets | List datasets
*DatasetApi* | [**status**](docs/DatasetApi.md#status) | **GET** /api/v1/datasets/{datasetId}/status | List dataset status
*DatasetApi* | [**status_all**](docs/DatasetApi.md#status_all) | **GET** /api/v1/datasets/status | List status for all datasets
*DatasetApi* | [**update**](docs/DatasetApi.md#update) | **PUT** /api/v1/datasets/{datasetId} | Update a dataset
*DatasetApi* | [**update_converter_pipeline**](docs/DatasetApi.md#update_converter_pipeline) | **PUT** /api/v1/datasets/{datasetId}/converters | Update converter pipeline
*DocumentExportApi* | [**download**](docs/DocumentExportApi.md#download) | **GET** /api/v1/collections/{collectionId}/export/{jobId}/content | Download exported document
*DocumentExportApi* | [**get_job**](docs/DocumentExportApi.md#get_job) | **GET** /api/v1/collections/{collectionId}/export/{jobId} | Get status of a job
*DocumentExportApi* | [**list**](docs/DocumentExportApi.md#list) | **GET** /api/v1/collections/{collectionId}/export | List doucment export jobs
*DocumentExportApi* | [**submit**](docs/DocumentExportApi.md#submit) | **POST** /api/v1/collections/{collectionId}/export | Request document export
*EnrichmentApi* | [**create**](docs/EnrichmentApi.md#create) | **POST** /api/v1/enrichments | Create an enrichment
*EnrichmentApi* | [**create_facet_dictionary**](docs/EnrichmentApi.md#create_facet_dictionary) | **POST** /api/v1/enrichments/{enrichmentId}/fdics | Create a dictionary
*EnrichmentApi* | [**create_from_pear**](docs/EnrichmentApi.md#create_from_pear) | **POST** /api/v1/enrichments#pear | Create an enrichment from pear file
*EnrichmentApi* | [**delete**](docs/EnrichmentApi.md#delete) | **DELETE** /api/v1/enrichments/{enrichmentId} | Delete an enrichment
*EnrichmentApi* | [**get**](docs/EnrichmentApi.md#get) | **GET** /api/v1/enrichments/{enrichmentId} | List enrichment details
*EnrichmentApi* | [**get_facet_dictionary**](docs/EnrichmentApi.md#get_facet_dictionary) | **GET** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId} | List dictionary details
*EnrichmentApi* | [**get_facet_dictionary_content**](docs/EnrichmentApi.md#get_facet_dictionary_content) | **GET** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId}/content | Fetch a dictionary content
*EnrichmentApi* | [**get_reg_ex_config**](docs/EnrichmentApi.md#get_reg_ex_config) | **GET** /api/v1/enrichments/{enrichmentId}/regexconfig | Get the regular expression annotator rules
*EnrichmentApi* | [**list**](docs/EnrichmentApi.md#list) | **GET** /api/v1/enrichments | List enrichments
*EnrichmentApi* | [**list_facet_dictionaries**](docs/EnrichmentApi.md#list_facet_dictionaries) | **GET** /api/v1/enrichments/{enrichmentId}/fdics | List dictionaries
*EnrichmentApi* | [**remove_facet_dictionary**](docs/EnrichmentApi.md#remove_facet_dictionary) | **DELETE** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId} | Remove a dictionary
*EnrichmentApi* | [**update**](docs/EnrichmentApi.md#update) | **PUT** /api/v1/enrichments/{enrichmentId} | Update an enrichment
*EnrichmentApi* | [**update_facet_dictionary**](docs/EnrichmentApi.md#update_facet_dictionary) | **PUT** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId} | Update a dictionary
*EnrichmentApi* | [**update_facet_dictionary_content**](docs/EnrichmentApi.md#update_facet_dictionary_content) | **PUT** /api/v1/enrichments/{enrichmentId}/fdics/{dictionaryId}/content | Update a dictionary content
*EnrichmentApi* | [**update_reg_ex_config**](docs/EnrichmentApi.md#update_reg_ex_config) | **PUT** /api/v1/enrichments/{enrichmentId}/regexconfig | Create or update regular expression annotator rules
*ExplorationApi* | [**query**](docs/ExplorationApi.md#query) | **GET** /api/v1/explore/{collectionId}/query | Searches for documents
*ExplorationApi* | [**querymodifier**](docs/ExplorationApi.md#querymodifier) | **GET** /api/v1/explore/{collectionId}/querymodifier | Searches for documents
*FileResourceApi* | [**create**](docs/FileResourceApi.md#create) | **POST** /api/v1/fileResources | Create a file resource
*FileResourceApi* | [**delete**](docs/FileResourceApi.md#delete) | **DELETE** /api/v1/fileResources/{fileResourceId} | Delete a file resource
*FileResourceApi* | [**download**](docs/FileResourceApi.md#download) | **GET** /api/v1/fileResources/{fileResourceId}/download | Fetch a file resource content
*FileResourceApi* | [**get**](docs/FileResourceApi.md#get) | **GET** /api/v1/fileResources/{fileResourceId} | List file resource details
*FileResourceApi* | [**list**](docs/FileResourceApi.md#list) | **GET** /api/v1/fileResources | List file resources
*FileResourceApi* | [**update**](docs/FileResourceApi.md#update) | **PUT** /api/v1/fileResources/{fileResourceId} | Update a file resource
*FileResourceApi* | [**upload**](docs/FileResourceApi.md#upload) | **POST** /api/v1/fileResources/{fileResourceId}/upload | Update a file resource content
*GroupApi* | [**create_group**](docs/GroupApi.md#create_group) | **POST** /api/v1/usermgmt/groups | Create group
*GroupApi* | [**delete_group**](docs/GroupApi.md#delete_group) | **DELETE** /api/v1/usermgmt/groups/{name} | Remove group
*GroupApi* | [**get_group**](docs/GroupApi.md#get_group) | **GET** /api/v1/usermgmt/groups/{name} | Get group
*GroupApi* | [**list_groups**](docs/GroupApi.md#list_groups) | **GET** /api/v1/usermgmt/groups | List groups
*GroupApi* | [**list_user_in_group**](docs/GroupApi.md#list_user_in_group) | **GET** /api/v1/usermgmt/groups/{name}/users | List users in a group
*GroupApi* | [**update_group**](docs/GroupApi.md#update_group) | **PUT** /api/v1/usermgmt/groups/{name} | Update group
*ImporterApi* | [**add_csv**](docs/ImporterApi.md#add_csv) | **PUT** /api/v1/importer/csv/upload/{uploadId} | Add a CSV file
*ImporterApi* | [**create**](docs/ImporterApi.md#create) | **POST** /api/v1/datasets/{datasetId}/importers | Create an importer
*ImporterApi* | [**delete**](docs/ImporterApi.md#delete) | **DELETE** /api/v1/datasets/{datasetId}/importers/{importerId} | Delete an importer
*ImporterApi* | [**delete_csv**](docs/ImporterApi.md#delete_csv) | **DELETE** /api/v1/importer/csv/upload/{uploadId}/{fileName} | Delete a CSV file
*ImporterApi* | [**get**](docs/ImporterApi.md#get) | **GET** /api/v1/datasets/{datasetId}/importers/{importerId} | List importer details
*ImporterApi* | [**get_configuration_template**](docs/ImporterApi.md#get_configuration_template) | **GET** /api/v1/importer/types/{importerType} | List importer configuration
*ImporterApi* | [**get_types**](docs/ImporterApi.md#get_types) | **GET** /api/v1/importer/types | List importer types
*ImporterApi* | [**list**](docs/ImporterApi.md#list) | **GET** /api/v1/datasets/{datasetId}/importers | List importers
*ImporterApi* | [**list_csv**](docs/ImporterApi.md#list_csv) | **GET** /api/v1/importer/csv/upload/{uploadId} | List CSV files
*ImporterApi* | [**preview_csv**](docs/ImporterApi.md#preview_csv) | **POST** /api/v1/importer/csv/preview/{uploadId}/{fileName} | Preview CSV file
*ImporterApi* | [**start**](docs/ImporterApi.md#start) | **POST** /api/v1/datasets/{datasetId}/importers/{importerId}/start | Start an importer
*ImporterApi* | [**status**](docs/ImporterApi.md#status) | **GET** /api/v1/datasets/{datasetId}/importers/{importerId}/status | List importer status
*ImporterApi* | [**stop**](docs/ImporterApi.md#stop) | **POST** /api/v1/datasets/{datasetId}/importers/{importerId}/stop | Stop an importer
*ImporterApi* | [**update**](docs/ImporterApi.md#update) | **PUT** /api/v1/datasets/{datasetId}/importers/{importerId} | Update an importer
*ImporterApi* | [**upload_csv**](docs/ImporterApi.md#upload_csv) | **POST** /api/v1/importer/csv/upload | Upload CSV file
*LabelerApi* | [**cancel_model_training**](docs/LabelerApi.md#cancel_model_training) | **DELETE** /api/v1/labelers/{labelerId}/models/{modelId}/task | Cancel labeler model training task
*LabelerApi* | [**create**](docs/LabelerApi.md#create) | **POST** /api/v1/labelers | Create a labeler
*LabelerApi* | [**create_collection**](docs/LabelerApi.md#create_collection) | **POST** /api/v1/labelers/{labelerId}/collection | Create and set a collection
*LabelerApi* | [**create_model_from_source_dataset**](docs/LabelerApi.md#create_model_from_source_dataset) | **POST** /api/v1/labelers/{labelerId}/models/all | Create a labeler model
*LabelerApi* | [**delete**](docs/LabelerApi.md#delete) | **DELETE** /api/v1/labelers/{labelerId} | Delete a labeler
*LabelerApi* | [**get**](docs/LabelerApi.md#get) | **GET** /api/v1/labelers/{labelerId} | Show labeler details
*LabelerApi* | [**get_enrichment**](docs/LabelerApi.md#get_enrichment) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/enrichments | List enrichments where the labeler model deployed
*LabelerApi* | [**get_enrichment_latest**](docs/LabelerApi.md#get_enrichment_latest) | **GET** /api/v1/labelers/{labelerId}/models/latest/enrichments | List enrichments where the latest labeler model deployed
*LabelerApi* | [**get_model**](docs/LabelerApi.md#get_model) | **GET** /api/v1/labelers/{labelerId}/models/{modelId} | Show labeler model details
*LabelerApi* | [**get_model_latest**](docs/LabelerApi.md#get_model_latest) | **GET** /api/v1/labelers/{labelerId}/models/latest | Show the latest labeler model details
*LabelerApi* | [**get_model_status**](docs/LabelerApi.md#get_model_status) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/status | Show labeler model status
*LabelerApi* | [**get_resource_set**](docs/LabelerApi.md#get_resource_set) | **GET** /api/v1/labelers/{labelerId}/resources/{resourceSetId} | Show labeler resource set details
*LabelerApi* | [**get_test_eval**](docs/LabelerApi.md#get_test_eval) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/test | Show test evaluation result of the model
*LabelerApi* | [**get_test_evals**](docs/LabelerApi.md#get_test_evals) | **GET** /api/v1/labelers/{labelerId}/test-evals | List test evaluation results
*LabelerApi* | [**get_validation_eval**](docs/LabelerApi.md#get_validation_eval) | **GET** /api/v1/labelers/{labelerId}/models/{modelId}/validation | Show validation evaluation result of the model
*LabelerApi* | [**list**](docs/LabelerApi.md#list) | **GET** /api/v1/labelers | List labelers
*LabelerApi* | [**set_model**](docs/LabelerApi.md#set_model) | **PUT** /api/v1/labelers/{labelerId}/models | Set a labeler model
*LabelerApi* | [**set_resource_set**](docs/LabelerApi.md#set_resource_set) | **PUT** /api/v1/labelers/{labelerId}/resources | Set a labeler resource set
*LabelerApi* | [**update**](docs/LabelerApi.md#update) | **PUT** /api/v1/labelers/{labelerId} | Update a labeler
*MigrationApi* | [**convert_cas_to_index**](docs/MigrationApi.md#convert_cas_to_index) | **POST** /api/v1/migration/cas2index | Migrate CAS to index mapping file
*MigrationApi* | [**convert_category_tree**](docs/MigrationApi.md#convert_category_tree) | **POST** /api/v1/migration/category | Migrate category tree file
*MigrationApi* | [**convert_csv_to_fdic**](docs/MigrationApi.md#convert_csv_to_fdic) | **POST** /api/v1/migration/csv2fdic | Migrate dictionary CSV file
*MigrationApi* | [**convert_fdic**](docs/MigrationApi.md#convert_fdic) | **POST** /api/v1/migration/fdic | Migrate dictionary file
*NLPApi* | [**analyze**](docs/NLPApi.md#analyze) | **POST** /api/v1/collections/{collectionId}/analyze | Analyze documents with enrichments of a specified collection
*RankerApi* | [**create**](docs/RankerApi.md#create) | **POST** /api/v1/rankers | Create a ranker instance
*RankerApi* | [**delete**](docs/RankerApi.md#delete) | **DELETE** /api/v1/rankers/{rankerInstanceId} | Delete a ranker instance
*RankerApi* | [**get**](docs/RankerApi.md#get) | **GET** /api/v1/rankers/{rankerInstanceId} | Show ranker instance details
*RankerApi* | [**list**](docs/RankerApi.md#list) | **GET** /api/v1/rankers | List ranker instances
*RankerApi* | [**update**](docs/RankerApi.md#update) | **PUT** /api/v1/rankers/{rankerInstanceId} | Update a ranker instance
*SimilarDocumentRankerApi* | [**cancel_model_training**](docs/SimilarDocumentRankerApi.md#cancel_model_training) | **DELETE** /api/v1/sdrankers/{rankerId}/models/{modelId}/task | Cancel ranker model training task
*SimilarDocumentRankerApi* | [**create**](docs/SimilarDocumentRankerApi.md#create) | **POST** /api/v1/sdrankers | Create a similar document ranker
*SimilarDocumentRankerApi* | [**create_collection**](docs/SimilarDocumentRankerApi.md#create_collection) | **POST** /api/v1/sdrankers/{rankerId}/collection | Create and set a collection
*SimilarDocumentRankerApi* | [**create_model_from_source_dataset**](docs/SimilarDocumentRankerApi.md#create_model_from_source_dataset) | **POST** /api/v1/sdrankers/{rankerId}/models/all | Create a similar document ranker model
*SimilarDocumentRankerApi* | [**delete**](docs/SimilarDocumentRankerApi.md#delete) | **DELETE** /api/v1/sdrankers/{rankerId} | Delete a ranker
*SimilarDocumentRankerApi* | [**get**](docs/SimilarDocumentRankerApi.md#get) | **GET** /api/v1/sdrankers/{rankerId} | Show similar document ranker details
*SimilarDocumentRankerApi* | [**get_instances**](docs/SimilarDocumentRankerApi.md#get_instances) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId}/instances | List ranker instances where the model deployed
*SimilarDocumentRankerApi* | [**get_instances_latest**](docs/SimilarDocumentRankerApi.md#get_instances_latest) | **GET** /api/v1/sdrankers/{rankerId}/models/latest/instances | List ranker instances where the latest ranker model deployed
*SimilarDocumentRankerApi* | [**get_model**](docs/SimilarDocumentRankerApi.md#get_model) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId} | Show similar document ranker model details
*SimilarDocumentRankerApi* | [**get_model_latest**](docs/SimilarDocumentRankerApi.md#get_model_latest) | **GET** /api/v1/sdrankers/{rankerId}/models/latest | Show the latest similar document ranker model details
*SimilarDocumentRankerApi* | [**get_model_status**](docs/SimilarDocumentRankerApi.md#get_model_status) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId}/status | Show ranker model status
*SimilarDocumentRankerApi* | [**get_resource_set**](docs/SimilarDocumentRankerApi.md#get_resource_set) | **GET** /api/v1/sdrankers/{rankerId}/resources/{resourceSetId} | Show ranker resource set details
*SimilarDocumentRankerApi* | [**get_test_evals**](docs/SimilarDocumentRankerApi.md#get_test_evals) | **GET** /api/v1/sdrankers/{rankerId}/test-evals | List ranking evaluation results
*SimilarDocumentRankerApi* | [**get_test_rank_eval**](docs/SimilarDocumentRankerApi.md#get_test_rank_eval) | **GET** /api/v1/sdrankers/{rankerId}/models/{modelId}/test-rank | Show ranking evaluation result of the model
*SimilarDocumentRankerApi* | [**list**](docs/SimilarDocumentRankerApi.md#list) | **GET** /api/v1/sdrankers | List similar document rankers
*SimilarDocumentRankerApi* | [**set_model**](docs/SimilarDocumentRankerApi.md#set_model) | **PUT** /api/v1/sdrankers/{rankerId}/models | Set a similar document ranker model
*SimilarDocumentRankerApi* | [**set_resource_set**](docs/SimilarDocumentRankerApi.md#set_resource_set) | **PUT** /api/v1/sdrankers/{rankerId}/resources | Set a ranker resource set
*SimilarDocumentRankerApi* | [**update**](docs/SimilarDocumentRankerApi.md#update) | **PUT** /api/v1/sdrankers/{rankerId} | Update a similar document ranker
*SystemApi* | [**download_logs**](docs/SystemApi.md#download_logs) | **GET** /api/v1/system/logs/download | Get logs in CSV format.
*SystemApi* | [**download_service_logs**](docs/SystemApi.md#download_service_logs) | **GET** /api/v1/system/logs/service | Download service logs for IBM support.
*SystemApi* | [**export_config**](docs/SystemApi.md#export_config) | **GET** /api/v1/system/config/{type}/{id} | Export configuration and resources
*SystemApi* | [**get_logs**](docs/SystemApi.md#get_logs) | **GET** /api/v1/system/logs | Get logs in JSON format.
*SystemApi* | [**get_usage**](docs/SystemApi.md#get_usage) | **GET** /api/v1/system/usage | Get system usage
*SystemApi* | [**import_config**](docs/SystemApi.md#import_config) | **POST** /api/v1/system/config | Import configuration and resources
*UserApi* | [**change_my_password**](docs/UserApi.md#change_my_password) | **POST** /api/v1/usermgmt/user/changemypassword | Helps the user change his password
*UserApi* | [**change_user_password**](docs/UserApi.md#change_user_password) | **POST** /api/v1/usermgmt/user/changeuserpassword | Helps the admin change user&#39;s password
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /api/v1/usermgmt/user | Create user (or Grant Access if an External LDAP is present 
*UserApi* | [**delete_config_file**](docs/UserApi.md#delete_config_file) | **DELETE** /api/v1/usermgmt/config/file/{name} | Delete config file
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /api/v1/usermgmt/user/{username} | Delete user
*UserApi* | [**do_logout**](docs/UserApi.md#do_logout) | **GET** /api/v1/usermgmt/logout | Logs out current logged in user from session
*UserApi* | [**get_admin_patterms**](docs/UserApi.md#get_admin_patterms) | **GET** /api/v1/usermgmt/config/admin | Get list of pattern texts to make user as Admin
*UserApi* | [**get_config_file**](docs/UserApi.md#get_config_file) | **GET** /api/v1/usermgmt/config/file/{name} | Get config file
*UserApi* | [**get_current_user_info**](docs/UserApi.md#get_current_user_info) | **GET** /api/v1/usermgmt/user/currentUserInfo | Get current user info
*UserApi* | [**get_user_by_name**](docs/UserApi.md#get_user_by_name) | **GET** /api/v1/usermgmt/user/{username} | Get user details by user name
*UserApi* | [**list_config_file**](docs/UserApi.md#list_config_file) | **GET** /api/v1/usermgmt/config/file/ | List config files
*UserApi* | [**list_users**](docs/UserApi.md#list_users) | **GET** /api/v1/usermgmt/users | Get all users
*UserApi* | [**put_admin_patterns**](docs/UserApi.md#put_admin_patterns) | **POST** /api/v1/usermgmt/config/admin | Put list of pattern texts to make user as Admin
*UserApi* | [**signin_user**](docs/UserApi.md#signin_user) | **POST** /api/v1/usermgmt/login | Logs user into the system
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /api/v1/usermgmt/user/{username} | Update user record (including his password/hash)
*UserApi* | [**upload_config_file**](docs/UserApi.md#upload_config_file) | **POST** /api/v1/usermgmt/config/file/{name} | Upload config file
*UserApi* | [**user_sign_up**](docs/UserApi.md#user_sign_up) | **POST** /api/v1/usermgmt/signup | User requesting access
*UserApi* | [**validate_user**](docs/UserApi.md#validate_user) | **GET** /api/v1/usermgmt/validate | Almost an alias to the signin method. but intended for REST APIs


## Documentation For Models

 - [Annotation](docs/Annotation.md)
 - [AnnotationIndexingSpecType](docs/AnnotationIndexingSpecType.md)
 - [AnnotationIndexingSpecs](docs/AnnotationIndexingSpecs.md)
 - [AsFacetType](docs/AsFacetType.md)
 - [Category](docs/Category.md)
 - [ClassifierModel](docs/ClassifierModel.md)
 - [ClassifierModelStatus](docs/ClassifierModelStatus.md)
 - [Collection](docs/Collection.md)
 - [CollectionParams](docs/CollectionParams.md)
 - [CollectionParamsDefaultOutput](docs/CollectionParamsDefaultOutput.md)
 - [CollectionParamsHighlighting](docs/CollectionParamsHighlighting.md)
 - [CollectionParamsQuery](docs/CollectionParamsQuery.md)
 - [CollectionParamsQuerymodifier](docs/CollectionParamsQuerymodifier.md)
 - [CollectionParamsSelect](docs/CollectionParamsSelect.md)
 - [CollectionStatus](docs/CollectionStatus.md)
 - [CollectionStatusDocproc](docs/CollectionStatusDocproc.md)
 - [CollectionStatusDocprocDatasets](docs/CollectionStatusDocprocDatasets.md)
 - [CollectionStatusDocprocJob](docs/CollectionStatusDocprocJob.md)
 - [ConfigFile](docs/ConfigFile.md)
 - [ConfigurationParameter](docs/ConfigurationParameter.md)
 - [ConfigurationParameterCondition](docs/ConfigurationParameterCondition.md)
 - [ConfigurationParameterEnum](docs/ConfigurationParameterEnum.md)
 - [ConfigurationParameterMatch](docs/ConfigurationParameterMatch.md)
 - [ConfigurationSection](docs/ConfigurationSection.md)
 - [ConfigurationTemplate](docs/ConfigurationTemplate.md)
 - [ConfigurationType](docs/ConfigurationType.md)
 - [ConverterConfiguration](docs/ConverterConfiguration.md)
 - [ConverterError](docs/ConverterError.md)
 - [ConverterPipelineConfiguration](docs/ConverterPipelineConfiguration.md)
 - [ConverterPipelineStatus](docs/ConverterPipelineStatus.md)
 - [Crawler](docs/Crawler.md)
 - [CrawlerConfiguration](docs/CrawlerConfiguration.md)
 - [CrawlerStatus](docs/CrawlerStatus.md)
 - [CrawlspaceStatus](docs/CrawlspaceStatus.md)
 - [Currency](docs/Currency.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetConfig](docs/DatasetConfig.md)
 - [DateFieldFormat](docs/DateFieldFormat.md)
 - [DiscoveredSubspace](docs/DiscoveredSubspace.md)
 - [Document](docs/Document.md)
 - [EnrichFieldGroup](docs/EnrichFieldGroup.md)
 - [Enrichment](docs/Enrichment.md)
 - [EntryType](docs/EntryType.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExportRequest](docs/ExportRequest.md)
 - [ExportResponse](docs/ExportResponse.md)
 - [ExportStatus](docs/ExportStatus.md)
 - [FacetDictionary](docs/FacetDictionary.md)
 - [FacetType](docs/FacetType.md)
 - [Features](docs/Features.md)
 - [Field](docs/Field.md)
 - [FileResource](docs/FileResource.md)
 - [FilterType](docs/FilterType.md)
 - [FlagDefinition](docs/FlagDefinition.md)
 - [FlagOption](docs/FlagOption.md)
 - [GeneralSettings](docs/GeneralSettings.md)
 - [GroupPattern](docs/GroupPattern.md)
 - [Importer](docs/Importer.md)
 - [IndexingConfig](docs/IndexingConfig.md)
 - [IngestionErrorResponse](docs/IngestionErrorResponse.md)
 - [IngestionStatus](docs/IngestionStatus.md)
 - [IngestionStatusSummary](docs/IngestionStatusSummary.md)
 - [InitDatasetConfig](docs/InitDatasetConfig.md)
 - [InitLabeler](docs/InitLabeler.md)
 - [InitSDRanker](docs/InitSDRanker.md)
 - [InputStream](docs/InputStream.md)
 - [IterableFacet](docs/IterableFacet.md)
 - [JsonNode](docs/JsonNode.md)
 - [LabelWiseClassifierMeasurements](docs/LabelWiseClassifierMeasurements.md)
 - [LabeledRange](docs/LabeledRange.md)
 - [Labeler](docs/Labeler.md)
 - [LabelerEvalResult](docs/LabelerEvalResult.md)
 - [ListDiscoveredSubspaces](docs/ListDiscoveredSubspaces.md)
 - [ListResponseCollection](docs/ListResponseCollection.md)
 - [ListResponseConfigurationType](docs/ListResponseConfigurationType.md)
 - [ListResponseCrawler](docs/ListResponseCrawler.md)
 - [ListResponseDataset](docs/ListResponseDataset.md)
 - [ListResponseEnrichment](docs/ListResponseEnrichment.md)
 - [ListResponseFileResource](docs/ListResponseFileResource.md)
 - [ListResponseImporter](docs/ListResponseImporter.md)
 - [ListResponseIngestionStatusSummary](docs/ListResponseIngestionStatusSummary.md)
 - [ListResponseLabeler](docs/ListResponseLabeler.md)
 - [ListResponseLabelerEvalResult](docs/ListResponseLabelerEvalResult.md)
 - [ListResponseRanker](docs/ListResponseRanker.md)
 - [ListResponseRankerEvalResult](docs/ListResponseRankerEvalResult.md)
 - [ListResponseSDRanker](docs/ListResponseSDRanker.md)
 - [ListResponseString](docs/ListResponseString.md)
 - [ListResponseTestit](docs/ListResponseTestit.md)
 - [LogRecord](docs/LogRecord.md)
 - [LogRecords](docs/LogRecords.md)
 - [MLCollection](docs/MLCollection.md)
 - [MacroAvgClassifierMeasurements](docs/MacroAvgClassifierMeasurements.md)
 - [Metadata](docs/Metadata.md)
 - [MicroAvgClassifierMeasurements](docs/MicroAvgClassifierMeasurements.md)
 - [MultiFieldMap](docs/MultiFieldMap.md)
 - [NLPDocument](docs/NLPDocument.md)
 - [Number](docs/Number.md)
 - [PathComponentType](docs/PathComponentType.md)
 - [PreviewResult](docs/PreviewResult.md)
 - [QueryResult](docs/QueryResult.md)
 - [QueryResultFacetCounts](docs/QueryResultFacetCounts.md)
 - [QueryResultFacetStats](docs/QueryResultFacetStats.md)
 - [QueryResultResponse](docs/QueryResultResponse.md)
 - [QueryResultResponseHeader](docs/QueryResultResponseHeader.md)
 - [Ranker](docs/Ranker.md)
 - [RankerEvalResult](docs/RankerEvalResult.md)
 - [RankerMeasurements](docs/RankerMeasurements.md)
 - [RegExConfig](docs/RegExConfig.md)
 - [RegExRule](docs/RegExRule.md)
 - [ResourceSet](docs/ResourceSet.md)
 - [RichDocument](docs/RichDocument.md)
 - [RichField](docs/RichField.md)
 - [SDRanker](docs/SDRanker.md)
 - [Schedule](docs/Schedule.md)
 - [SimpleResponse](docs/SimpleResponse.md)
 - [SizeInfo](docs/SizeInfo.md)
 - [SizeList](docs/SizeList.md)
 - [Stats](docs/Stats.md)
 - [SystemUsage](docs/SystemUsage.md)
 - [SystemUsageDatasetMetrics](docs/SystemUsageDatasetMetrics.md)
 - [SystemUsageDatasetMetricsDatasets](docs/SystemUsageDatasetMetricsDatasets.md)
 - [SystemUsageNlpMetrics](docs/SystemUsageNlpMetrics.md)
 - [SystemUsageNlpMetricsCollections](docs/SystemUsageNlpMetricsCollections.md)
 - [Testit](docs/Testit.md)
 - [UpdateInterval](docs/UpdateInterval.md)
 - [UploadResult](docs/UploadResult.md)
 - [User](docs/User.md)
 - [UserGroup](docs/UserGroup.md)
 - [ValType](docs/ValType.md)
 - [ValidationMetrics](docs/ValidationMetrics.md)
 - [WordType](docs/WordType.md)
 - [ZkIngestionStatus](docs/ZkIngestionStatus.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author



