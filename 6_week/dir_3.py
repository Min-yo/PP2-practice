import os
if os.path.exists(r".\Test\test.txt"):
    print(os.path.basename(r".\Test\test.txt"))
    print(os.path.dirname(r'.\Test\test.txt'))
    
#print(os.access(r'.\Test\test.txt', os.F_OK))