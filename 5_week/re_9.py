import re
st = 'StringToTestThisCase'
print(' '.join(re.findall(r'[A-Z]{1}[a-z]+', st)))