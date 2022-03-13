import os
if os.access(r'.\Test\test2.txt', os.F_OK):
    os.remove(r'.\Test\test2.txt')
    
'''
if os.path.exsist('twxt.txt'):
    
'''