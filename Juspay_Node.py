'''
Question
========

You are given a forest (it may contain a single tree or more than one tree) with N nodes.

Each node is given an integer value 0 to (N­-1).

You have to find:

===================

The depth of forest at which maximum number of nodes are present.

N can be very large. Aim for an algorithm with a time complexity of O(N).

INPUT FORMAT

=================

An integer T, denoting the number of testcases, followed by 2T lines, as each testcase will contain 2 lines.

First line of each testcase has the value of N.

Second line of each testcase has list of N values where the number at index i is the parent of node i. The parent of root is -1. ( The index has the range [0, N­-1] ).

OUTPUT FORMAT

===============

For each testcase given, output a single line that has the depth of forest at which maximum number of nodes are present. If multiple depths has same number of nodes, then deepest depth should be selected.

SAMPLE INPUT

==============

2

6

5 -1 1 1 5 2

13

4 3 -1 -1 1 2 7 3 1 4 2 1 2

SAMPLE OUTPUT

====================

3

1

'''


t = int(input('Enter the Number of test cases : '))
n = [0 for i in range(t)]
s = [0 for i in range(t)]
for test in range(t):
    n[test] = int(input('Enter the Number of elements in tree for tree '+str(test+1)+' : '))
    s[test] = list(map(int,input('Enter the elements of tree '+str(test+1)+' separeted by space : ').split()))

for test in range(t):
    l = [[] for i in range(n[test])]
    visited = [0 for i in range(n[test])]

    for i in range(n[test]):
        if s[test][i] == -1:
            l[0].append(i)
            visited[i] = 1

    for i in range(n[test]):
        for j in range(len(l[i])):
            for k in range(len(s[test])):
                if l[i][j] == s[test][k] and visited[k] == 0:
                    l[i+1].append(k)
    max = 0
    pos = None
    for i in range(len(l)):
        if len(l[i]) >= max:
            pos = i
            max = len(l[i])

    print(pos)