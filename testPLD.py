import ast
from PLD2 import PLD

compare = {}
for key,value in PLD.items():
    if value != []:
        list1 = PLD[key]
        list2 = eval('ast.{0}._fields'.format(key))
        set1 = set(list1)
        set2 = set(list2)
        if set1 == set2:
            pass
        else:
            print(key,value)