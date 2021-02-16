from azure.identity import ClientSecretCredential 
from azure.mgmt.authorization import AuthorizationManagementClient
from msrestazure.azure_active_directory import AADTokenCredentials
import adal

authority_host_uri = 'https://login.microsoftonline.com'
tenant = '72f988bf-86f1-41af-91ab-2d7cd011db47'
authority_uri = authority_host_uri + '/' + tenant
resource_uri = 'https://management.core.windows.net/'
client_id = 'fd2bfb66-5b4c-492e-8f39-44699600bca8'
subscription_id = 'bac420ed-c6fc-4a05-8ac1-8c0c52da1d6e'
client_secret = 'nBQ0.q_i76XQn_318O-sk19.la_UswC-9c'

credential = ClientSecretCredential(
    tenant_id=tenant,
    client_id=client_id,
    client_secret=client_secret
)

context = adal.AuthenticationContext(authority_uri, api_version=None)
code = context.acquire_user_code(resource_uri, client_id)
print(code['message'])
mgmt_token = context.acquire_token_with_device_code(resource_uri, code, client_id)
credentials = AADTokenCredentials(mgmt_token, client_id)
authorizationClient = AuthorizationManagementClient(credential, subscription_id)
roles = authorizationClient.role_assignments.list()
for role in roles:
    print(role)