'''
Raw: user login count
Snake Case: user_login_count
Camel Case: userLoginCount
'''
import re
st_snake = 'string_in_snake_case'
def toUp(ch):
    ch = ch.group(0)
    if ch.islower():
        return re.sub(r'_', '', ch.upper())
    else:
        return ch

print(re.sub(r'_[a-zA-Z]', toUp, st_snake))