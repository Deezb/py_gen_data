import pickle
from PLD2 import PLD

with open('filename.pickle', 'rb') as file_handle:
    nodevalues = pickle.load(file_handle)

# def get_sub_list(a_node):
#     child_nodes = []
#     child_node_numbers = a_node[1]
#     for child_node in child_node_numbers:
#         child_nodes.append(nodevalues[child_node])
#     return child_nodes
#
#
# def get_sub_node(typeinfo, from_node):
#     child_nodes = get_sub_list(from_node)
#     for node in child_nodes:
#         if typeinfo == node[2].split('.')[-1]:
#             return node
#         return "Error Node {0} not found in {1}".format(typeinfo, from_node)


def dicty(top = 0 ):
    a_dict = {}
    a_dict[top] = {}
    currentHead = nodevalues[top]

    # if this node has no children take its information
    if currentHead[1] == []:
        a_dict[top][currentHead[2].split('.')[-1]] = currentHead[4]
        return a_dict

    # if this node has children, add their dicts to this dict
    children = currentHead[1]
    newdict = {}
    for child in children:
        a_dict[top][child] = dicty(child)[child]
        a_dict.update(newdict)
    return a_dict


def get_PLD_sub_nodes(from_node):
    sub_nodes = {}

    node_type = from_node[3]
    if '_ast' in node_type:
        node_name = node_type[13:-2]
        sub_nodes[from_node] = PLD[node_name]
    if sub_nodes:
        for node in sub_nodes:
            get_PLD_sub_nodes(node)
        return sub_nodes
    else:
        return


def extract_function_defs():
    func_def_list = []
    symbol_dict = {}
    children = []
    for node in nodevalues:
        if node[3] == "<class '_ast.FunctionDef'>":
            func_def_list.append(node)

    for funcnode in func_def_list:
        node_number, node_child_list, node_text_value, node_type, node_value = funcnode
        children = get_sub_list(funcnode)
    args = get_sub_node('args', children)

    print(children)

def strip(dicty):
    for key, value in dicty.items:
        pass




def main():
    gosh = dicty(2)
    dicty2 = strip(dicty)
    print(gosh)
    #extract_function_defs()


if __name__=='__main__':
    main()