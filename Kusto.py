from azure.kusto.data import KustoClient, KustoConnectionStringBuilder
from azure.kusto.data.exceptions import KustoServiceError
from azure.kusto.data.helpers import dataframe_from_result_table
import pandas as pd

AAD_TENANT_ID = "72f988bf-86f1-41af-91ab-2d7cd011db47"
KUSTO_CLUSTER = "https://help.kusto.windows.net/"
KUSTO_DATABASE = "Samples"

KCSB = KustoConnectionStringBuilder.with_aad_device_authentication(
    KUSTO_CLUSTER)
KCSB.authority_id = AAD_TENANT_ID

KUSTO_CLIENT = KustoClient(KCSB)
KUSTO_QUERY = "StormEvents | project StartTime,State, EventType| sort by StartTime desc | take 10"

try:
    RESPONSE = KUSTO_CLIENT.execute(KUSTO_DATABASE, KUSTO_QUERY)
except KustoServiceError as error: 
     print("Error : ", error)   

#print(RESPONSE.primary_results[0])
df = dataframe_from_result_table(RESPONSE.primary_results[0])
jsonData = df.to_json()
print(jsonData)
