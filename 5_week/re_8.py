import re
st = 'StringToTestThisCase'
#print(re.findall(r'[A-Z]{1}[a-z]+', st))

print(re.split(r'([A-Z]{1}[a-z]+)', st)) #([A-Z]{1}[a-z]+) == ([A-Z][^A-Z]*)