# -*- coding: utf-8 -*-
"""task2(2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZNmCPqm8b6Fsqkpu85JTbe-Kk833F3A
"""

def merge(a, b, m, n):
    new = [None] * (m+n)
    i = 0
    j = 0
    k = 0
    while i<m and j<n:
        if a[i] < b[j]:
            new[k] = a[i]
            i += 1
            k += 1
        else:
            new[k] = b[j]
            j += 1
            k += 1
    while i < m:
        new[k] = a[i]
        i += 1
        k += 1
    while j < n:
        new[k] = b[j]
        j += 1
        k += 1
    ln = ""
    for i in range(len(new)-1):
        ln += str(new[i]) + " "
    ln += str(new[len(new)-1])
    outfile.writelines(ln)

infile = open("/content/drive/MyDrive/cse221_ass02/input2(2).txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass02/output2(2).txt", "w")

lis = infile.readlines()
m = int(lis[0])
a = list(map(int, lis[1].split(" ")))
n = int(lis[2])
b = list(map(int, lis[3].split(" ")))
merge(a, b, m, n)

