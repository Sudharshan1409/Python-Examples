'''
if input : APPLE,
then
output should be : E L (reverse of last two letters of the word)
'''
#code area
def convert(word):
    return word[-1] + ' ' + word[-2]




if __name__ == '__main__':
    word = input()
    result = convert(word)
    print(result)