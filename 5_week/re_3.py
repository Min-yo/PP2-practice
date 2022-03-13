import re
patt = r'[a-z]+_{1}[a-z]+'
if re.search(patt, input()):
    print('Match')
else:
    print('No')