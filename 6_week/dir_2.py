import os
print('Exist:', os.access('.', os.F_OK))
print('Readable:', os.access('.', os.R_OK))
print('Writable:', os.access('.', os.W_OK))
print('Executable:', os.access('.', os.X_OK))