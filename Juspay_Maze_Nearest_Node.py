n = int(input('Enter the length of the list : '))
l = list(map(int,input('Enter the elements : ').split()))
source,destination = map(int,input('Enter the Source and Destination : ').split())

if len(l) != n:
    print('Error')
    exit()
ele = None
d = []
s = []
src,dest = source,destination
while True:
    if src == -1 or dest == -1:
        print('Nearest Node for both source and destination is ' + str(ele))
        exit()
    if l[src] < len(l) and l[dest] < len(l):
        src = l[src]
        dest = l[dest]
    if src in d:
        ele = src
    elif dest in s:
        ele = dest
    elif src == dest:
        ele = src
    if ele:
        print('Nearest Node for both source and destination is ' + str(ele))
        exit()
    elif src in s or dest in d:
        print('There is no Nearest node for given source and destination')
        exit()
    else:
        d.append(dest)
        s.append(src)
