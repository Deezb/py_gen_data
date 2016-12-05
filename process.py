import pickle
# from PLD2 import PLD
from pprint import pprint as pp

with open('filename2.pickle', 'rb') as file_handle:
    nodevalues = pickle.load(file_handle)


def dicty(top=0):
    current_head = nodevalues[top]
    node_name = current_head[4]+'>>'+current_head[2].split('.')[-1]
    a_dict = {}
    a_dict[node_name] = {}

    # if this node has no children, extract its information
    if current_head[1] == []:
        # if the information exists, use it, don't add empty
        if current_head[5]:  #current_head[5] is the stored value of the node
            a_dict[node_name] = current_head[5]
        if a_dict[node_name]:
            return a_dict
        else:
            return None

    # if this node has children, add their dicts to this dict
    children = current_head[1]
    newdict = {}
    for child in children:
        child_dict = dicty(child)
        child_name = nodevalues[child][4]+'>>'+nodevalues[child][2].split('.')[-1]
        if child_dict:
            child_d = child_dict[child_name]
        else:
            child_d = None
        if child_dict:
            a_dict[node_name][child_name] = child_d
        newdict.update(a_dict)
    if newdict:
        return newdict
    else:
        return None


def get_function(ntype, values):

    adict = dict()
    bdict = dict()
    if isinstance(values, dict):
        for key, value in values.items():
            if ntype in key:
                bdict = get_function(ntype, value)
            adict.update(bdict)
    return adict


def strip_function(values):

    args = get_function('args', values)
    body = get_function('body', values)
    name = get_function('name', values)
    decorator_list = get_function('decorator_list', values)
    returns = get_function('returns', values)
    print('args = ', args, body, name, decorator_list, returns)


def process(tree):

    function_declaration= [node for node in nodevalues if node[4] == "FunctionDef"]
    for item in function_declaration:
        strip_function(item)


def main():

    view_dict = dicty(0)
    pp(view_dict)
    dicty2 = process(view_dict)
    print(dicty2)


if __name__ == '__main__':
    main()
