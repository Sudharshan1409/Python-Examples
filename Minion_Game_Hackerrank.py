import time
def isvowel(a):
    if a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U':
        return True
    else:
        return False

def minion_game(string):
    stuart = []
    kevin = []
    for i in range(len(string)):
        if isvowel(string[i]):
            s = ''
            for j in range(i,len(string)):
                s += string[j]
                kevin.append(s)
        else:
            s = ''
            for j in range(i,len(string)):
                s += string[j]
                stuart.append(s)
    if len(stuart) > len(kevin):
        print('Strart '+str(len(stuart)))
    else:
        print('Kevin '+str(len(kevin)))



if __name__ == '__main__':
    s = input()
    start = time.time()
    minion_game(s)
    end = time.time()
    print()
    print(end-start)