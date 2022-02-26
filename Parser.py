from contextlib import nullcontext
import this

from ast import ClassDecl, Method, objCreation


class Parser:

    def __init__(self) -> None:
        self.index = 0
        self.tokens = None
        self.expr = []

    def advance(self):
        self.index += 1

    def peep(self):
        return self.tokens[self.index + 1]

    def current(self):
        return self.tokens[self.index]

    def parse(self, tokens):
        self.tokens = tokens
        while self.current().type == "EOF":
            self.expr.push(self.statements())
        return self.expr

    def statements(self):
        current = self.current()
        if current.value == "class":
            return self.classDeclarations()
        elif self.tokens[self.index + 3].value == "new":
            return self.objectCreation()

    def expression(self):
        return self.add()

    def classDeclarations(self):
        self.advance()
        className = self.current().value
        while self.current().type == "LBRACE":
            self.advance()

        self.advance()
        methods = []
        while self.current().type != "RBRACE" and self.tokens[self.index + 1].type != "EOF":
            methods.extend(self.classMethods())
        self.advance()
        return ClassDecl(className, methods)

    def classMethods(self):
        type = None
        if self.current().value == "static":
            type = self.current().value
            self.advance()
        methodName = self.current().value
        self.advance()
        while self.current().type != "LBRACE":
            self.advance()
        return Method(methodName, type, self.blockStatements())

    def blockStatement(self):
        self.advance()
        statements = []
        while self.current().type != "RBRACE" and self.tokens[self.index + 1].type != "EOF":
            statements.extend(self.statements())
            self.advance()
        self.advance()
        return [statements]
    # Animal dog = new Animal()

    def objectCreation(self):
        className = self.current().value
        self.advance()
        varName = self.current().value
        self.advance()
        return objCreation(className, varName)
