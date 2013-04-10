import string, sys
class Token(object):
    def __init__(self, ttype, value):
        self.__type = ttype
        self.__value = value
    def __str__(self):
        return '(' + self.__type + ',\'' + str(self.__value) + '\')'
def read_tokens(fn):
    with open(fn) as f:
        t=["",""];s=0;tl=[]
        c=f.read(1)
        while c!="":
            if c==" " or c=="\n":
                if not t[s]=="" and s==1:
                    tl.append(Token(t[0],t[1]));t = ["",""];s = 0
            elif c == ":": side=1 
            else:
                t[s] = t[s] + c
            char = fp.read(1)
    return tl    
def main(a):
    c = len(a)
    if 2>c:
        print('Usage: python3 hw3.py input.txt'); return 1
    tokens = read_tokens(argv[1])
    for token in tokens: print(token)
    return 0
if __name__ == '__main__':
    sys.exit(main(sys.argv))
