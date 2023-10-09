import io
import sys

str_list = []
filename = sys.argv[1]
with open(sys.argv[1],'r') as f:
    str_list = list(f.read())

with open(sys.argv[1],'w') as f:
    i = 0
    while i<len(str_list):
        str_list.insert(i+64,'\n')
        i += 64
    f.write(''.join(str_list))