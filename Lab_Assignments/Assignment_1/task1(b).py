# -*- coding: utf-8 -*-
"""task1(b).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vRWx4BP__DHB2IUv6S6ophtdimag2Edj
"""

#Task_1(b)
inf = open("/content/drive/MyDrive/cse221_ass01/input1b.txt", "r")
opf = open("/content/drive/MyDrive/cse221_ass01/output1b.txt", "w")
ins = inf.readlines()
n = int(ins[0])
lines = ""
for i in range(1, n+1):
    ins[i] = ins[i].strip("\n")
    tmp = ins[i].split()
    num1 = int(tmp[1])
    num2 = int(tmp[3])
    if tmp[2] == "+":
        s = num1 + num2
    elif tmp[2] == "-":
        s = num1 - num2
    elif tmp[2] == "*":
        s = num1 * num2
    elif tmp[2] == "/":
        s = num1 / num2
    exp = tmp[1] +" "+tmp[2]+" "+tmp[3]
    if i != n:
        l = f"The result of {exp} is {s}\n"
    else:
        l =  f"The result of {exp} is {s}"
    lines += l
opf.writelines(lines)