# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZNmCPqm8b6Fsqkpu85JTbe-Kk833F3A
"""

infile = open("/content/drive/MyDrive/cse221_ass07/input2_1.txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass07/output2_1.txt", "w")
l = infile.readlines()
nm = list(map(int, l[0].split(" ")))
n = nm[0]
m = nm[1]
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
def scheduler(s):
    res = []
    rem_elem = []
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
            rem_elem.append(i)
            s.remove(i)
        rem = []
    return res, rem_elem

t = s
t, r = scheduler(t)
c = len(t)
for i in range(m-1):
    t, r = scheduler(r)
    c += len(t)
outfile.writelines(str(c))