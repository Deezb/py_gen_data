import ast
from matplotlib import pyplot as plt
# common = { 'col_offset', 'lineno'}
# Python Language Dictionary = PLD refers to Python version - 3.5.2
from PLD2 import PLD
import collections

def add_to_list(base, sep, bits):
    return [sep.join([base, bit]) for bit in bits]


class SourceTree(object):

    def __init__(self):
        from textfile import text
        self.text = text
        self.tree = ast.parse(self.text)
        self.head = self.tree
        self.name = 'tree'
        self.parent_array = {}
        self.child_array = {}
        self.end_list = []
        self.count = 0
        self.queue = [(self.count, self.name)]

    def add_to_endlist(self, item):

        self.end_list.append(item)

    def queue_peek(self):

        return self.queue[0]

    def queue_add(self, item):
        self.queue.append(item)

    def queue_del(self, item):

        try:
            self.queue.remove(item)
        except:
            print(item," was not found in the queue list, but attempt was made to remove. called by queue_del(child)")

    def get_child_of(self, item):
        number, value = item
        return self.child_array[number]

    def get_parent_of(self, item):
        number, value = item
        return self.parent_array[number]

    def get_children_of(self, item):
        (count, parent_full_name) = item
        child_list = [(count, parent_full_name)]
        print('starting analysis of ', parent_full_name)
        parent_is_list = eval('isinstance(self.{0}, list)'.format(parent_full_name))
        if parent_is_list:
            child_list_len = len(eval('self.'+parent_full_name))
            list_of_children = list(map(lambda x: '[{0}]'.format(x), range(child_list_len)))
            child_list.extend(add_to_list(parent_full_name, '', list_of_children))
            print('children from list 	', child_list)
        else:
            parent = eval('type(self.{0})'.format(parent_full_name))
            parent_value = str(parent)
            parent_value2 = (parent_value)[13:-2] if parent_value.startswith("<class '_ast.") else parent_value[
                                                                                                       8:-2]
            if parent_value2 in PLD:
                sub_list = PLD[parent_value2]
                for unit in sub_list:
                    child_list.append('.'.join([parent_full_name, unit]))
            else:
                print("'",parent_value2, "' is not in the PLD dictionary ")
                print("child_list returning for '{0}' analysis = {1}".format(parent_full_name, child_list))
        return child_list

    def print_out(self):
        for row in sorted(self.end_list):
            rowl = len(str(row[1]))
            print(row[0], ' ' * (60 - rowl), row[1], ' ', eval('self.'+row[1]))

    def mainrun(self):
        while len(self.queue) > 0:
            parent_sent = self.queue[0]
            current_nodes_children = self.get_children_of(parent_sent)
            for child in current_nodes_children:
                current_count = self.count
                if child == parent_sent:
                    print(child, ' has returned')
                    self.add_to_endlist(parent_sent)
                    current_parent = parent_sent[0]
                    self.queue_del(child)
                else:
                    print(child, ' is a new node for the queue list')
                    self.count += 1
                    self.queue_add((self.count, child))
                    self.parent_array[self.count] = current_parent
                    self.child_array.setdefault(current_parent, []).append(self.count)
            print('queue list currently holds : ', self.queue)
            print('end_list currently holds : ', self.end_list)
            print('Node count is at ', self.count)
        print('end result = ', self.end_list)
        print('The Parent reference dictionary contains :',self.parent_array)
        print('The Children reference dictionary contains :',self.child_array)
        self.print_out()
        return self.end_list, self.child_array, self.parent_array


class Depth(object):
    def __init__(self, end_list, carray, parray):
        self.parray = parray
        self.carray = carray
        self.depth_dict= { 0 : 1 }
        self.clen = len(end_list)

    def get_depth(self, item):
        if item in self.depth_dict.keys():
            self.depth = self.depth_dict[item]
        else:
            self.depth = 1 + self.get_depth(self.parray[item])
            self.depth_dict[item] = self.depth
        return self.depth

    def run(self):
        for item in self.parray:
            self.get_depth(item)
        print(self.depth_dict)
        return self.depth_dict


def main():
    structure = SourceTree()
    endl, car, par = structure.mainrun()
    depths  = Depth(endl,car,par)
    node_depths = depths.run()
    nodes_at_depth = {}
    for key,value in node_depths.items():
        print('node depths = ',value, key)
        nodes_at_depth.setdefault(value, []).append(key)

    print('nodes at a depth', nodes_at_depth)
    layer_widths = [(key,len(value)) for key,value in nodes_at_depth.items()]
    print(layer_widths)
    print('max width is {0} node columns, with {1} rows'.format(max([val[1] for val in layer_widths]), len(layer_widths)))



if __name__=='__main__':
    main()



