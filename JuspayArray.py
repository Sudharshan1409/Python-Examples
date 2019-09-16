path = []
p = []
count = 0
def path_count(l,source,destination,x,y):
    global path
    global p
    global count
    if x == destination[0] and y == destination[1]:
        p.append((destination[0],destination[1]))
        path.append(p)
        p = []
        count += 1
        return
    
    if x > destination[0] or y > destination[1]:
        return
    
    if l[x][y] == 1:
        return
    p.append((x,y))
    path_count(l,source,destination,x+1,y)
    path_count(l,source,destination,x,y+1)
    

m,n = map(int,input('Enter the dimension of the matrix : ').split())
l = [[0 for j in range(n)] for i in range(m)]
ones = []
o = list(input('Enter : ').split())
for i in o:
    ones.append(tuple(map(int,i.split(','))))

for i in ones:
    l[i[0]][i[1]] = 1


source = tuple(map(int,input('Enter the source node value : ').split()))

destination = tuple(map(int,input('Enter the destination node value : ').split()))

print('The Matrix you entered is as follows : \n\n')


for i in l:
    print('\t\t',end = '')
    for j in i:
        print(j,end = '   ')
    print('\n')
print('\n')

path_count(l,source,destination,source[0],source[1])

print(path)
print(f"\n\nCount = {len(path),count}")



