# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZNmCPqm8b6Fsqkpu85JTbe-Kk833F3A
"""

infile = open("/content/drive/MyDrive/cse221_ass07/input1_3.txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass07/output1_3.txt", "w")
l = infile.readlines()
l[0] = l[0].strip("\n")
n = int(l[0])
s = []
for i in range(1, len(l)):
    l[i] = l[i].strip("\n")
    elem = l[i]
    subs = list(map(int, elem.split(" ")))
    s.append(subs)
for i in range(len(s)):
    for j in range(0, len(s)-i-1):
        if s[j][1] > s[j+1][1]:
            s[j], s[j+1] = s[j+1], s[j]
res = []
while len(s) > 0:
    fst = s[0]
    res.append(fst)
    s.remove(fst)
    rem = []
    for i in range(len(s)):
        st = s[i]
        s1 = []
        s2 = []
        for k in range(fst[0], fst[1]+1):
            s1.append(k)
        for j in range(st[0], st[1]+1):
            s2.append(j)
        if s1[len(s1)-1] == s2[0]:
            s1 = s1[0: len(s1)-1]
            s2 = s2[1 : len(s2)]
        for m in s1:
            if m in s2:

                rem.append(st)
                break
    for i in rem:
        s.remove(i)
    rem = []
line = ""
for i in res:
    ll = ""
    for j in i:
        ll += str(j) + " "
    ll += "\n"
    line += ll
outfile.writelines(line)