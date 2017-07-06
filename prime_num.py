#!/usr/bin/python3
# 文件名：client.py

lower=int(input('input the lower value:'))
upper=int(input('input the upper value:'))

for i in range(lower, upper+1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            print(i, end=', ')


