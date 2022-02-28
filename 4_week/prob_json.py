import json
 
with open("sample-data.json") as jsonFile:
    data = json.load(jsonFile)
    jsonFile.close()


print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in data["imdata"]:
    dn = i['l1PhysIf']['attributes']['dn']
    descr = i['l1PhysIf']['attributes']['descr']
    speed = i['l1PhysIf']['attributes']['speed']
    mtu = i['l1PhysIf']['attributes']['mtu']
    print(dn + '                             '+ descr +' '+ speed + '   ' + mtu)



'''
for i in data['emp_details']:
    print(i)

>> topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
'''
