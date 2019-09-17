''' pangram problem 
all of a,b,c,d,.....z and ' ' must be present in the sentence given '''

#code area
def pangram_convert(strings):
    l = []
    s = ''
    for i in range(97,123):
        l.append(chr(i))
    l.append(' ')
    for i in strings:
        found = True
        for j in l:
            if j not in i:
                found = False
        if found:
            s += '1'
        else:
            s += '0'
    return s
    





if __name__ == '__main__':
    n = int(input())
    strings = []
    for i in range(n):
        strings.append(input())
    result = pangram_convert(strings)
    print(result)