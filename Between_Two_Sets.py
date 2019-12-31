# You will be given two arrays of integers and asked to determine all integers 
# that satisfy the following two conditions:

# --> The elements of the first array are all factors of the integer being considered
# --> The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. 
# You must determine how many such numbers exist.

# Input Format:
# First line consists of elements of array a
# Second line consists of elements of array b

# Output Format:
# Print the number of integers that are considered to be between a and b.

def find_lcm(a):
    l = []
    p = [2,3,5,7,11,13,17,19,23,29]
    i = 0
    while i < len(p):
        mod = False
        if a:
            for j in range(len(a)):
                if a[j] % p[i] == 0:
                    mod = True
                    a[j] = a[j] // p[i]
            if mod:
                l.append(p[i])
            else:
                i += 1
            while True:
                if 1 in a:
                    a.remove(1)
                else:
                    break
        else:
            break
    lcm = 1
    if a:
        for i in a:
            lcm *= i
    for i in l:
        lcm *= i
    return lcm

def getTotalX(a,b):
    lcm = find_lcm(a)
    lcms = []
    i = 2
    lcms.append(lcm)
    while True:
        if lcms[-1] > min(b):
            lcms.pop(-1)
            break
        else:
            lcms.append(lcm * i)
            i += 1
    count = 0
    for i in range(len(lcms)):
        flag = True
        for j in b:
            if j % lcms[i] != 0:
                flag = False
        if flag:
            count += 1
    return count

if __name__ == '__main__':
    a = list(map(int,input('\nEnter the Elements of Array A : ').split()))
    b = list(map(int,input('\nEnter the Elements of Array B : ').split()))

    print('Number of integers that are considered to be between a and b are : ',getTotalX(a,b))
             