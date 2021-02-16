import os
from azure.identity import ClientSecretCredential 
from azure.mgmt.authorization import AuthorizationManagementClient

subscription_id = '96f7a6ad-39d4-42e5-b676-a510a9e6fd22'
tenant_id = '72f988bf-86f1-41af-91ab-2d7cd011db47'
client_id = 'fd2bfb66-5b4c-492e-8f39-44699600bca8'
client_secret = 'nBQ0.q_i76XQn_318O-sk19.la_UswC-9c'

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

authorizationClient = AuthorizationManagementClient(credential, subscription_id)
roles = authorizationClient.role_assignments.list()
for role in roles:
    print(role)