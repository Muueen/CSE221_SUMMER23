# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxWCOdGs2ef3fbPXEPlt_bW-J1OzMX4I
"""

def maxy(a, b, f):
    if f== 0:
        if arr[a] > arr[b]:
            return a
        else:
            return b
    else:
        if abs(arr[a]) > abs(arr[b]):
            return a
        else:
            return b

def findMax(arr, l, r, f):
    if l == r:
        return l

    mid = (l + r) // 2

    left_max = findMax(arr, l, mid, f)
    right_max = findMax(arr, mid + 1, r, f)

    return maxy(left_max, right_max, f)

infile = open("/content/drive/MyDrive/cse221_ass03/input2.txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass03/output2.txt", "w")
l = infile.readlines()
l[0] = l[0].strip("\n")
n = int(l[0])
l[1] = l[1].strip("\n")
arr = list(map(int, l[1].split(" ")))

idx_j = findMax(arr, 1, len(arr)-1, 1)
max_j = arr[idx_j]
idx_i = findMax(arr, 0, idx_j-1, 0)
max_i = arr[idx_i]
res = str(max_i + max_j**2)
outfile.writelines(res)