import re
patt = r'^a(b*)$'
if re.search(patt, input()):
    print('Match')
else:
    print('No')