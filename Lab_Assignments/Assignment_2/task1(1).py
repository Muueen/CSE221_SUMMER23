# -*- coding: utf-8 -*-
"""task1(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZNmCPqm8b6Fsqkpu85JTbe-Kk833F3A
"""

infile = open("/content/drive/MyDrive/cse221_ass02/input1(1).txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass02/output1(1).txt", "w")

lis = infile.readlines()
NS = list(map(int, lis[0].split(" ")))
inp = list(map(int, lis[1].split(" ")))
f = 0
for i in range(len(inp)):
    for j in range(len(inp)):
        s = 0
        if i != j:
            s = inp[i] + inp[j]
        if s == NS[1]:
            lin = f"{i+1} {j+1}"
            outfile.writelines(lin)
            f = 1
            break
    if f == 1:
        break
if f == 0:
    outfile.writelines("IMPOSSIBLE")