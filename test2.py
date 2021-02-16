from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

subscription_id = '96f7a6ad-39d4-42e5-b676-a510a9e6fd22'
tenant_id = '72f988bf-86f1-41af-91ab-2d7cd011db47'
client_id = 'fd2bfb66-5b4c-492e-8f39-44699600bca8'
client_secret = 'nBQ0.q_i76XQn_318O-sk19.la_UswC-9c'

credential = ClientSecretCredential(
    tenant_id=tenant_id,
    client_id=client_id,
    client_secret=client_secret
)

compute_client = ComputeManagementClient(
    credential=credential,
    subscription_id=subscription_id
)


vms = compute_client.virtual_machines.list_all()

myvm_resource_group=""

for vm in vms:
    if vm.name == VM_NAME:
        print(vm.id)

        #the vm.id is always in this format: 
        #'/subscriptions/your_subscription_id/resourceGroups/your_resource_group/providers/Microsoft.Compute/virtualMachines/your_vm_name'
        #so you can split it into list, and the resource_group_name's index is always 4 in this list.
        temp_id_list=vm.id.split('/')
        myvm_resource_group=temp_id_list[4]

print("**********************!!!!!!!!!!")

print("the vm test0's resource group is: " + myvm_resource_group)

# now you know the vm name and it's resourcegroup, you can use other methods,
# like compute_client.virtual_machines.get(resource_group_name, vm_name) to do any operations for this vm.