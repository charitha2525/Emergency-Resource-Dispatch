resource_request=[]
n=int(input("enter the size of the resource"))
resource_request=[0]*n
for i in range(n):
    resource_request[i]=int(input("enter the resource"))
print(resource_request)
invalid_request=[]
low_demand=[]
moderate_demand=[]
high_demand=[]
valid_entries=0
invalid_entries=0
for i in range(n):
    if resource_request[i]<0:
        invalid_request=invalid_request+[resource_request[i]]
        invalid_entries=invalid_entries+1
    elif resource_request[i]==0:
        print("no demand")
        valid_entries=valid_entries+1
    elif resource_request[i]>=1 and resource_request[i]<=20:
        low_demand=low_demand+[resource_request[i]]
        valid_entries=valid_entries+1
    elif resource_request[i]>=21 and resource_request[i]<=50:
        moderate_demand=moderate_demand+[resource_request[i]]
        valid_entries=valid_entries+1
    else:
        high_demand=high_demand+[resource_request[i]]
        valid_entries=valid_entries+1
print("before personalization")
print("invalid-request",invalid_request)
print("low-demand",low_demand)
print("moderate-demand",moderate_demand)
print("high-demand",high_demand)

reg=int(input("enter the register number"))
print("register number:",reg)
if reg%3==0:
    removed=len(high_demand)
    high_demand=[]
elif reg%3==1:
    removed=len(low_demand)
    low_demand=[]
else:
    removed=len(invalid_request)
    invalid_request=[]
print("after personalization")
print("invalid-request",invalid_request)
print("low-demand",low_demand)
print("moderate-demand",moderate_demand)
print("high-demand",high_demand)
print("final report")
print("invalid entries",invalid_entries)
print("valid entries",valid_entries)
print("removed due to personalization",removed)


