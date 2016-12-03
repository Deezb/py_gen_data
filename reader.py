import ast
from textfile import text


class stack_paren(object):
    def __init__(self):
        self.indent = 0
        self.count = 0
        self.stack = []

class stack_brack(object):
    def __init__(self):
        self.count = 0
        self.stack = []


class stack_squar(object):
    def __init__(self):
        self.count = 0
        self.stack = []


def getStructs():
    # push (  pop )
    stackParen = stack_paren()

    # push>>{  pop>>}
    #stackBrack = stack_brack()

    # push>>[ pop>>]
    #stackSquar = stack_squar()
    return stackParen

def unitise(stack, sent):
    old_letter = ""
    word = ""
    for letter in sent:
        if letter in ['(','[','{']:
            stack.stack.append((stack.count,stack.indent, word))
            word = ""
            stack.count += 1
            stack.indent += 1

        elif letter in [')', ']', '}']:

            if old_letter in ['(','[','{']:
                current = stack.stack.pop()
                stack.stack.append((current[0],current[1],current[2]+old_letter+letter))
                stack.count -= 1
                stack.indent -= 1
            else:
                if word != "":
                    stack.stack.append((stack.count, stack.indent, word))
                word = ""
                stack.count += 1
                stack.indent -= 1
        elif letter in [',']:
            word += letter
            stack.stack.append((stack.count, stack.indent, word))
            word = ""
            stack.count += 1
        else:
            word += letter
        old_letter = letter
    stack = sorted(list(stack.stack))

    return stack

def output(prin):
    for line in prin:
        line_number , indent, value = line
        print(line_number ,indent*'\t', value)



def main():

    # first bring in the text from the external file
    # then parse the text into an AST.
    tree = ast.parse(text)

    # next the tree is dumped to a string
    sent = ast.dump(tree)

    print(type(sent))
    structs = getStructs()

    prin = unitise(structs, sent)
    #now the string is split by brackets into sections
    output(prin)




if __name__=='__main__':
    main()



