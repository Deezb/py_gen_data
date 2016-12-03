import ast
##common = { 'col_offset', 'lineno'}
# Python Language Dictionary = PLD refers to Python version - 3.5.2
from PLD2 import PLD, PLDLIST
from textfile import text as text
tree = ast.parse(text)

def add_to_list(base, sep, bits):

    """
    this function takes a base text and a list of addons, at returns a list of concatenated strings
    example ('hello', '#', '['world','there'] => ['hello#world','hello#there']
    example ('tree', '.' , ['body','name','orelse']) => ['tree.body', 'tree.name', 'tree.orelse']
    """
    return [sep.join([base, bit]) for bit in bits]



def tie_in(endlist):

    """
    this function prints the columns of output data in a 2 column format with a
    right aligned left column and a left aligned right column
    :param endlist: the list of source tokens with it tree location
    :return: prints output no returned value
    """
    for row in sorted(endlist):
        rowl = len(str(row[1]))
        print(' '*(60-rowl),row[1],' ',eval(row[1]))

def get_children_of( parent_full_name):
    """
    This method takes in a nodename and checks if that nodename is a list
    if it is a list it returns each sub-node in the list.
    else it returns the list of dictionary lookups for that token type.
    :param parent_full_name:
    :return:
    """
    """this function takes any object and returns a list of its children
        children are nodes that do not contain dunders"""
    child_list = [parent_full_name]

    print('starting analysis of ',parent_full_name)
    parent_is_list = eval('isinstance({0}, list)'.format(parent_full_name))

    if parent_is_list:

        child_list_len = len(eval(parent_full_name))
        list_of_children = list(map(lambda x : '[{0}]'.format(x),range(child_list_len)))
        child_list.extend(add_to_list(parent_full_name, '', list_of_children))
        print('children from list ', child_list)

    else:

        parent = eval('type({0})'.format(parent_full_name))
        parent_value = str(parent)
        parent_value2 = (parent_value)[13:-2] if parent_value.startswith("<class '_ast.") else parent_value[8:-2]
        if parent_value2 in PLD:
            sub_list = PLD[parent_value2]
            for item in sub_list:
                child_list.append('.'.join([parent_full_name, item]))

        else:
            print('not found in PLD ',parent_value2)
        print('returning child_list for {0} = {1}'.format(parent_full_name, child_list))
    return child_list


def main():
    count = 0
    stacker = ['tree']
    endlist=[]
    parent_array ={
        1 : 0,
    }

    child_array ={
        0 : [1],
    }

    while len(stacker) > 0:
        item = stacker[0]
        parent_sent = item

        current_items_children = get_children_of(item)
        for child in current_items_children:
            current_count = count
            if child == parent_sent:
                print(child, ' has returned')
                endlist.append((count, child))

                stacker.remove(child)
            else:
                print(child,' is new for stacker')
                count += 1
                stacker.append(child)
                parent_array[count] = current_count
                child_array.setdefault(current_count, []).append(count)
        print('stack currently holds : ',stacker)
        print('endlist currently holds : ', endlist)
        print('count is at ', count)
    print('end result = ', endlist)
    goget = tie_in(endlist)

if __name__=='__main__':
    main()
