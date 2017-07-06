#!/usr/bin/python3
# 文件名：enumregkeys.py
# function search keyword in register keys and entries from a register file and save matched keys to a new file.
# the input file must be utf-8 encoding

from collections import defaultdict
import sys

file_path = sys.argv[1] #r'F:\Python\samples\Registry_pre_030717.reg'
kw = sys.argv[2]
output_file = r'F:\Python\samples\output.reg'
f=open(file_path, 'r',encoding='utf-8')
fo = open(output_file, 'w')
lines = f.readlines()
regs = defaultdict(list)
keyname = ''

for i in lines:
    #print(i)
    if(i[0] == '['):#and (i.find('6F7ED54FB2908B548B9F9DA38432FF4F') != -1):
        keyname = i
        #print(i)
    else:
        regs[keyname].append(i)
oregs = defaultdict(list)
for k, v in regs.items():
    if (k.find(kw) != -1):
        print(k)
        oregs[k] = v
    else:
        for value in v:
            if (value.find(kw) != -1):
                oregs[k] = v
                break

for k, v in oregs.items():
    fo.write(k)
    for value in v:
        fo.write(value)

f.close()
fo.close()
