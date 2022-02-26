
class ClassDecl:
    def __init__(self, clsName, methods):
        self.clsName = clsName
        self.methods = methods

    def visit(self, visitor):
        return visitor.visitClassDecl(self)


class Method:
    def __init__(self, name, type1, body, argument_list):
        self.name = name
        self.type = type1
        self.body = body
        self.argument_list = argument_list


class BodyBlock:
    def __init__(self, listOfVar, listOfIfElse, listOfForLoop, listOfWhileLoop):
        self.listOfVar = listOfVar
        self.listOfIfElse = listOfIfElse
        self.listOfForLoop = self.listOfForLoop
        self.listOfWhileLoop = self.listOfWhileLoop

class forLoopBlock:
    def __init__(self, count_name, count_value, operand, constraint_value, increment):
        self.count_name = count_name
        self.count_value = count_value
        self.operand = operand
        self.constraint_value = constraint_value
        self.increment = increment

class variableAssignmentBlock:
    def __init__(self, var_name, var_value):
        self.var_name = var_name
        self.var_value = var_value

class objCreation:
    def __init__(self, className, varName):
        self.className = className
        self.varName = varName

class ifElseStatement:
    def __init__(self, statements):
        self.statements = statements
