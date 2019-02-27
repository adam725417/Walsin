# ExportRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | Query to specify documents to be exported | 
**fields** | **object** | Map of the fields to be exported. - CSV : Empty value makes field as column or name of the dimension table. - JSON: Ignored  | [optional] 
**facets** | **object** | Map of the facets to be exported. - CSV : Must be a name of the dimension table. - JSON: Ignored Note: Only facets on exported fields will be exported.  | [optional] 
**options** | **object** | Exporter options | [optional] 
**encoding** | **str** | Encoding of the output files | [optional] [default to 'UTF-8']
**tag** | **str** | Extra tag to filter jobs | [optional] 
**output_type** | **str** | Output plugin type | [optional] [default to 'CSV']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


