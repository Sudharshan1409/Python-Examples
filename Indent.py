import os
import sys
nl = 0
f = open(sys.argv[1],'r')
f1 = open('temp.txt','w')
tabs = 0
s = ''
def Tabs(tabs):
    global s
    for i in range(tabs):
        s += '\t'

for line in f:
    s = ''
    Tabs(tabs)
    for i in line:
        if i == '    ':
            pass
        elif i == '{':
            tabs += 1
            s += '\n'
            Tabs(tabs - 1)
            s += '{\n'
            Tabs(tabs)
        elif i == '}':
            tabs -= 1
            s += '\n'
            Tabs(tabs)
            s += '}\n'
            Tabs(tabs)
        elif i == '(':
            nl += 1
            s += i
        elif i == ')':
            nl -= 1
            s += i
        elif i == ';' and nl == 0:
            s += ';\n'
            Tabs(tabs)
        else:
            s += i 
    f1.write(s)

f1.close()
f.close()

f = open('temp.txt','r')
f1 = open(sys.argv[2],'w')

for line in f:
    if line.strip():
        f1.write(line)

os.system('rm temp.txt')

