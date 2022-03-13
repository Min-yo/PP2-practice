import re
patt = r'[A-Z]{1}[a-z]+'
if re.search(patt, input()):
    print('Match')
else:
    print('No')