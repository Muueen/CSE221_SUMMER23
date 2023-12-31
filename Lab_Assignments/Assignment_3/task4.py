# -*- coding: utf-8 -*-
"""task4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WxWCOdGs2ef3fbPXEPlt_bW-J1OzMX4I
"""

def partition(arr, l, r, piv_idx, n):
    arr[0], arr[piv_idx] = arr[piv_idx], arr[0]
    piv = arr[0]
    i = l
    for j in range(l+1, r+1):
        if arr[j] <= piv:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[i] = arr[i], arr[l]
    return arr[i], i

def finder(arr, m):
    m -= 1
    for i in range(len(arr)):
        n = partition(arr, 0, len(arr)-1, i, m)
        if n[1] == m:
            return n[0]

infile = open("/content/drive/MyDrive/cse221_ass03/input4.txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass03/output4.txt", "w")

l = infile.readlines()
for k in l:
    k = k.strip("\n")

lines = ""
n = int(l[0])
arr = list(map(int, l[1].split(" ")))
for i in  range(3, len(l)-1):
    m = int(l[i])
    lines += str(finder(arr, m)) + "\n"
m = int(l[len(l)-1])
lines += str(finder(arr, m))
outfile.writelines(lines)