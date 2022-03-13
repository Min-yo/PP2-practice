import re
patt = r'\s+|,+|[.]+'
s = input()
if re.search(patt, s):
    print(re.sub(patt, ':', s))
else:
    print('No')

#re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam And Something and This and That', flags=re.IGNORECASE)