# -*- coding: utf-8 -*-
"""task1A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZNmCPqm8b6Fsqkpu85JTbe-Kk833F3A
"""

infile = open("/content/drive/MyDrive/cse221_ass05/input1a_3.txt", "r")
outfile = open("/content/drive/MyDrive/cse221_ass05/output1a_3.txt", "w")

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
def dfs(node, graph, visited, stack, cycle):
    visited[node] = True
    cycle[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, graph, visited, stack, cycle):
                return True
        elif cycle[neighbor]:
            return True
    cycle[node] = False
    stack.append(node)
    return False

def topological_ord(n, graph):
    visited = [False] * (n+1)
    cycle = [False] * (n+1)
    stack = []

    for i in range(1, n+1):
        if not visited[i]:
            if dfs(i, graph, visited, stack, cycle):
                return "IMPOSSIBLE"

    return stack[::-1]

result = topological_ord(n, g)
line = ""
if result == "IMPOSSIBLE":
    line = "IMPOSSIBLE"
else:
    for i in range(len(result)-1):
        line += str(result[i]) + " "
    line += str(result[i+1])
outfile.writelines(line)