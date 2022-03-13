import re
patt = r'^a(b{2}|b{3})$'
if re.search(patt, input()):
    print('Match')
else:
    print('No')