sym = 'sym_'
from PLD2 import PLD

def not_a(item):
     result = False
     if item == None:
         result=True
     if item == []:
         result=True
     if item == {}:
         result=True
     return result

class Func_def(object):
    def __init__(self, node):
        self.head = node
        self.variables = []
        self.symbolic_variables = {}
        self.paths = []
        self.ifs = []
        self.code_tuples_list = []
        self.linecount = 0
        self.symbol_count = 0
        self.variable_count = 0
        self.active_ifs = []

    def add_symbols(self, *symbols):
        for symbol in symbols:
            self.symbolic_variables.append(sym+symbol)

    def add_variables(self, *variables):
        for variable in variables:
            self.variables.append(variable)

    def add_code(self, number, code):
        self.code_tuples_list.append((self.active_ifs,code))

    def start_if_bdy(self, if_id):
        if_id_bdy = str(if_id)+'_bdy'
        self.active_ifs.append(if_id_bdy)

    def start_if_els(self, if_id):
        if_id_bdy = str(if_id)+'_bdy'
        if_id_ore = str(if_id) + '_els'
        self.active_ifs.remove(if_id_bdy)
        self.active_ifs.append(if_id_ore)

    def end_if(self, if_id):
        if_id_ore = str(if_id) + '_els'
        self.active_ifs.remove(if_id)

    def read_thyself(self):
        args = self.head.args
        name = self.head.name
        body = self.head.body
        decorator_list = self.head.decorator_list
        ret = self.head.returns

        # Get all args from parameters
        arg_list = PLD['arguments'] # 3.5.2 => ['args', 'vararg', 'kwonlyargs', 'kw_defaults', 'kwarg', 'defaults']
        for arg in arg_list:
            fetch = eval('self.head.args.{0}'.format(arg))
            if not not_a(fetch):
                # that means it contains something, else is empty set or empty list or none
                if isinstance(fetch, list):
                    for arg in fetch:
                        self.variables.append(arg.arg)
                        self.symbolic_variables[arg.arg] = ('sym' + str(self.symbol_count))
                        self.symbol_count += 1
                if isinstance (fetch, str):
                    self.variables.append(fetch)
                    self.symbolic_variables[arg.arg] = ('sym' + str(self.symbol_count))
                    self.symbol_count += 1
        print(self.symbolic_variables)


