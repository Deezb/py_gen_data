import pickle
from PLD2 import PLD

with open('filename.pickle', 'rb') as file_handle:
    nodevalues = pickle.load(file_handle)


def dicty(top = 0 ):
    currentHead = nodevalues[top]
    node_name = currentHead[2].split('.')[-1]
    a_dict = {}
    a_dict[top] = {}

    # if this node has no children, extract its information
    if currentHead[1] == []:
        #if the information exists, use it, don't add empty
        if currentHead[4] and currentHead:
            a_dict[top][node_name] = currentHead[4]
        if a_dict[top]:
            return a_dict
        else:
            return None

    # if this node has children, add their dicts to this dict
    children = currentHead[1]
    newdict = {}
    for child in children:
        child_dict = dicty(child)
        if child_dict:
            child_d = child_dict[child]
        else:
            child_d = None
        if child_dict:
            a_dict[top][child] = child_d
        newdict.update(a_dict)
    if newdict:
        return newdict
    else:
        return None


def main():
    gosh = dicty(2)
    #dicty2 = strip(dicty)
    print(gosh)
    #extract_function_defs()
if __name__=='__main__':
    main()



#
#
# def extract_function_defs():
#     func_def_list = []
#     symbol_dict = {}
#     children = []
#     for node in nodevalues:
#         if node[3] == "<class '_ast.FunctionDef'>":
#             func_def_list.append(node)
#
#     for funcnode in func_def_list:
#         node_number, node_child_list, node_text_value, node_type, node_value = funcnode
#         children = get_sub_list(funcnode)
#     args = get_sub_node('args', children)


# def get_PLD_sub_nodes(from_node):
#     sub_nodes = {}
#
#     node_type = from_node[3]
#     if '_ast' in node_type:
#         node_name = node_type[13:-2]
#         sub_nodes[from_node] = PLD[node_name]
#     if sub_nodes:
#         for node in sub_nodes:
#             get_PLD_sub_nodes(node)
#         return sub_nodes
#     else:
#         return
#
# def strip(dictyd):
#     for key, value in dictyd.items:
#         pass
#
## def get_sub_list(a_node):
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


