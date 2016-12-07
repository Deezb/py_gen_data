from read2 import SourceTree
from read2 import ppnodes, pp, get_all_keys
from function_handler import Func_def
import pickle


def extract_funcs(node):
    """
    this function extracts all funcdefs and sets up the structure for creating
    the subsequent symbolic framework
    :return: list of FuncObjects
    """
    sn = [node[5] for node in node.nodevals if node[4] == 'FunctionDef']
    function_object_list = []
    for function_def_node in sn:
        new_function_object = Func_def(function_def_node)

        nfo = new_function_object
        nfo.read_thyself()
        print('a')



def main():
    structure = SourceTree()
    structure.mainrun()
    dic = structure.dictionary(0)
    nv = sorted(structure.nodevals, key=lambda x: x[2])
    ff = get_all_keys(dic)
    ff = sorted(ff)
    fg = [int(node.split('>>')[0]) for node in ff]
    fh = [node for node in structure.nodevals if node[0] in fg]

    ef = extract_funcs(structure)




    #
    #
    #
    # pp('max width is {0} node columns, with {1} rows'.format(max([val[1] for val in structure.layer_widths]), len(structure.layer_widths)))
    # print('structure.nodevals=', structure.nodevals)
    #
    # structure.ppdict(dic)
    #
    print(nv)
    #
    # print('fh', fh)
    # ppnodes(fh)
    # with open('filename2.pickle', 'wb') as file_handle:
    #     pickle.dump(structure.nodevals, file_handle)


if __name__ == '__main__':
    main()
