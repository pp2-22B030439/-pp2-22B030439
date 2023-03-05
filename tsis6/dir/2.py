import os
a = input()
print('Exist:', os.access(a, os.F_OK))