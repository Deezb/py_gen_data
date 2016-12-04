PLD = {
    'Module' : ['body'],
    'Num' : ['n'],
    'Str' : ['s'],
    'Bytes' : ['s'],
    'List' : ['elts','ctx'],
    'Tuple' : ['elts','ctx'],
    'Set' : ['elts'],
    'Dict' : ['keys','values'],
    'Ellipsis' : [],
    'NameConstant' : ['value'],
    'Name' : ['id','ctx'],
    'Load' : [],
    'Store' : [],
    'Del' : [],
    'Starred' : ['value','ctx'],
    'Expr' : ['value'],
    'UnaryOp' : ['op', 'operand'],
    'UAdd' : [],
    'USub' : [],
    'Not' : [],    # not keyword
    'Invert' : [], # ~ operator
    'BinOp' : ['left','op','right'],
    'Add' : [],
    'Sub' : [],
    'Mult' : [],
    'Div' : [],
    'FloorDiv' : [],
    'Mod' : [],
    'Pow' : [],
    'LShift' : [],
    'RShift' : [],
    'BitOr' : [],
    'BitXor' : [],
    'BitAnd' : [],
    'MatMult' : [], # new in 3.5 matrix multiplier '@'
    'BoolOp' : ['op','values'],
    'And' : [],
    'Or' : [],
    'Compare' : ['left','ops','comparators'], # ops is a list
    'Eq' : [],
    'NotEq' : [],
    'Lt' : [],
    'LtE' : [],
    'Gt' : [],
    'GtE' : [],
    'Is' : [],
    'IsNot' : [],
    'In' : [],
    'NotIn' : [],
    'Call' : ['func', 'args', 'keywords'],  #removed ,'starargs', 'kwargs' due to : AttributeError: 'Call' object has no attribute 'starargs'
    'keyword' : ['arg', 'value'],
    'IfExp' : ['test','body','orelse'], # all are Name nodes
    'Attribute' : ['value','attr','ctx'],
    'Subscript' : ['value','slice','ctx'],
    'Index' : ['value'],
    'Slice' : ['lower','upper','step'],
    'ExtSlice' : ['dims'],
    'ListComp' : ['elt','generators'],
    'SetComp' : ['elt','generators'],
    'GeneratorExp' : ['elt','generators'],
    'DictComp' : ['key','value','generators'],
    'comprehension' : ['target', 'iter', 'ifs'],
    'Assign' : ['targets', 'value'],
    'AugAssign' : ['target', 'op', 'value'],
    #'Print' : ['dest', 'values', 'nl'],
    'Raise' : ['exc', 'cause'],
    'Assert' : ['test', 'msg'],
    'Delete' : ['targets'],
    'Pass' : [],
    'Import' : ['names'],
    'ImportFrom' : ['module', 'names', 'level'],
    'alias' : ['name', 'asname'],
    'If' : ['test', 'body', 'orelse'],
    'For' : ['target', 'iter', 'body', 'orelse'],
    'While' : ['test', 'body', 'orelse'],
    'Break' : [],
    'Continue' : [],
    'Try' : ['body', 'handlers', 'orelse', 'finalbody'], 
    #'TryFinally' : ['body', 'finalbody'],              #have been removed
    #'TryExcept' : ['body', 'handlers', 'orelse'],      #have been removed
    'ExceptHandler' : ['type', 'name', 'body'],
    'With' : ['items', 'body'],
    'withitem' : ['context_expr', 'optional_vars'],
    'FunctionDef' : ['name', 'args', 'body', 'decorator_list', 'returns'],
    'Lambda' : ['args', 'body'],
    'arguments' : ['args', 'vararg', 'kwonlyargs', 'kwarg', 'defaults', 'kw_defaults'],
    'arg' : ['arg', 'annotation'],
    'Return' : ['value'],
    'Yield' : ['value'],
    'YieldFrom' : ['value'],
    'Global' : ['names'],
    'Nonlocal' : ['names'],
    'ClassDef' :['name', 'bases', 'keywords', 'body', 'decorator_list'],
    'AsyncFunctionDef' : ['name', 'args', 'body', 'decorator_list', 'returns'],
    'Await' : ['value'],
    'AsyncFor' : ['target', 'iter', 'body', 'orelse'],
    'AsyncWith' : ['items', 'body'],
    'Expression' : ['body'],
    'Suite' : ['body'],
}

PLDLIST = [     'body',
                'args',
                'arguments',
                'kw_defaults',
                'kwonlyargs',
                'starargs',
                'defaults',
                'targets',
                'values',
                'ops',
                'comparators',
                'orelse',
                'decorator_list',
            ]