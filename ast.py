
class ClassDecl:
    def __init__(self, clsName, methods):
        self.clsName = clsName
        self.methods = methods

    def visit(self, visitor):
        return visitor.visitClassDecl(self)


class Method:
    def __init__(self, name, type, body):
        self.name = name
        self.type = type
        self.body = body

class forLoopBlock:
    def __init__(self, count_name, count_value, operand, constraint_value, increment):
        self.count_name = count_name
        self.count_value = count_value
        self.operand = operand
        self.constraint_value = constraint_value
        self.increment = increment

class objCreation:
    def __init__(self, className, varName):
        self.clsname = className
        self.varName = varName


class ifElseStatement:
    def __init__(self, statements) -> None:
        self.statements = statements
