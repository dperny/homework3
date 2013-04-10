import string

class Token(object):
    def __init__(self, ttype, value):
        self.__type = ttype
        self.__value = value
    def __str__(self):
        return '(' + self.__type + ',\'' + str(self.__value) + '\')'

def read_tokens(filename):
    tokens = []
    with open(filename) as fp:
        token = ["",""]
        side = 0
        tokenlist = []
        char = fp.read(1)
        while not char == "":
            if char == " " or char == "\n":
                if not token[side] == "" and side == 1:
                    tokenlist.append(Token(token[0],token[1]))
                    token = ["",""]
                    side = 0
            elif char == ":": side = 1 
            else:
                token[side] = token[side] + char
            char = fp.read(1)
    return tokenlist
    
def main(argv):
    argc = len(argv)
    if 2 > argc:
        print('Usage: python3 hw3.py input.txt')
        return 1
    tokens = read_tokens(argv[1])
    for token in tokens:
        print(token)
    return 0
    
import sys
if __name__ == '__main__':
    sys.exit(main(sys.argv))
