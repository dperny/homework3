import string


class Token(object):

    def __init__(self, ttype, value):
        self.__type = ttype
        self.__value = value

    def __str__(self):
        return '(' + self.__type + ',\'' + str(self.__value) + '\')'



def read_tokens(filename):
    tokens = []

    #TODO: Open the file with the given filename.
    #TODO: Read the file one character at a time.
    #TODO: Create a Token object for each token.
    #TODO: Append each Token object to the tokens list.

    return tokens


def main(argv):
    argc = len(argv)
    if 2 > argc:
        print('Usage: python3 hw3.py input.txt')
        return 1

    #TODO: Store the tokens list returned by  read_tokens.
    #TODO: Print each Token in the tokens list.

    return 0


import sys
if __name__ == '__main__':
    sys.exit(main(sys.argv))
