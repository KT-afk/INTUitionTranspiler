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
    def __init__(self, type1):
        self.type = type1


class ForLoopBlock(BodyBlock):
    def __init__(self, count_name, count_value, operand, constraint_value, increment, type1):
        self.count_name = count_name
        self.count_value = count_value
        self.operand = operand
        self.constraint_value = constraint_value
        self.increment = increment
        self.type = type1


class VariableAssignmentBlock(BodyBlock):
    def __init__(self, var_name, var_value, type1):
        self.var_name = var_name
        self.var_value = var_value
        self.type = type1


class ObjCreationBlock(BodyBlock):
    def __init__(self, className, varName, type1):
        self.className = className
        self.varName = varName
        self.type = type1


class IfBlock(BodyBlock):
    def __init__(self, conditionVar, conditionOp, conditionVal, bodyList, type1):
        self.conditionVar = conditionVar
        self.conditionOp = conditionOp
        self.conditionVal = conditionVal
        self.bodyList = bodyList
        self.type = type1


class ElseBlock(BodyBlock):
    def __init__(self, bodyList, type1):
        self.bodyList = bodyList
        self.type = type1
