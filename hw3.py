import string

class Token(object):

    def __init__(self, ttype, value):
        self.__type = ttype
        self.__value = value

    def __str__(self):
        return '(' + self.__type + ',\'' + str(self.__value) + '\')'



def read_tokens(filename):
    tokens = []

    #TODONE: Open the file with the given filename.
    with open(filename) as fp:
        token = ["",""]
        side = 0
        tokenlist = []
        #TODO: Read the file one character at a time.
        char = fp.read(1)
        while not char == "":

            if char == " " or char == "\n":

                if not token[side] == "" and side == 1:
                    tokenlist.append(Token(token[0],token[1]))
                    token = ["",""]
                    side = 0
            # switch the side of token
            elif char == ":": side = 1 
            else:
                token[side] = token[side] + char
            char = fp.read(1)
        #TODONE: Create a Token object for each token.
        #TODONE: Append each Token object to the tokens list.
    return tokenlist


def main(argv):
    argc = len(argv)
    if 2 > argc:
        print('Usage: python3 hw3.py input.txt')
        return 1

    #TODONE: Store the tokens list returned by  read_tokens.
    tokens = read_tokens(argv[1])
    #TODONE: Print each Token in the tokens list.
    for token in tokens:
        print(token)

    return 0


import sys
if __name__ == '__main__':
    sys.exit(main(sys.argv))
