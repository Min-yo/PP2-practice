'''
Raw: user login count
Snake Case: user_login_count
Camel Case: userLoginCount
'''
import re
st_camel = 'stringInCamelCase'
def toLow(ch):
    ch = ch.group(0)
    if ch.isupper():
        st = '_' + str(ch.lower())
        return st
    else:
        return ch

print(re.sub(r'[A-Z]', toLow, st_camel))