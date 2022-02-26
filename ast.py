
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


class objCreation:
    def __init__(self, className, varName):
        self.clsname = className
        self.varName = varName


class ifElseStatement:
    def __init__(self, statements) -> None:
        self.statements = statements
