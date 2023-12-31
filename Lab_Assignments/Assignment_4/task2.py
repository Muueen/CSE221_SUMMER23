# -*- coding: utf-8 -*-
"""task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZRhVcdIIfr5cQOatRObMOeK463-HhA7Q
"""

class Queue:
    def __init__(self, n):
        self.q = [None]*n
        self.head = 0
        self.tail = 0
    def enq(self, elem):
        self.q[self.tail] = elem
        self.tail += 1
    def deq(self):
        temp = self.q[self.head]
        self.q[self.head] = None
        self.head += 1
        return temp
    def isEmpty(self):
        for i in self.q:
            if i != None:
                return False
        return True

infile = open("/content/drive/MyDrive/cse221_ass04/input2_3.txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass04/output2_3.txt", "w")

l = infile.readlines()
nm = list(map(int, l[0].split(" ")))
n = nm[0]
for elem in l:
    elem = elem.strip("\n")
def adjL(l):
    dic = {}
    for e2 in range(1, len(l)):
        l[e2] = list(map(int, l[e2].split(" ")))
        i = l[e2][0]
        j = l[e2][1]
        if i in dic:
            dic[i].append(j)
        else:
            dic[i] = [j]
        if j not in dic:
            dic[j] = []
    return dic
g = adjL(l)
def BFS_trvs(g, n):
    s = 1
    q = Queue(n)
    visited = [False] * (n+1)
    path = []
    q.enq(s)
    visited[s] = True
    while q.isEmpty() == False:
        for i in g[q.q[q.head]]:
            if visited[i] == False:
                q.enq(i)
                visited[i] = True
        el = q.deq()
        path.append(el)
    return path

path = BFS_trvs(g, n)
line = ""
for i in range(len(path)-1):
    line += str(path[i]) + " "
line += str(path[len(path)-1])
outfile.writelines(line)

