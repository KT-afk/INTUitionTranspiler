from contextlib import nullcontext
import this
import ast
from ast import ClassDecl, Method, objCreation, ifElseStatement


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
        while self.current()['type'] != "EOF":
            self.expr.extend(self.statements())
        return self.expr

    def statements(self):
        current = self.current()
        if current['value'] == "class":
            return self.classDeclarations()
        elif self.tokens[self.index + 3]['value'] == "new":
            return self.objectCreation()
        elif current['value'] == "if" or current['value'] == "else":
            return self.ifElseBlockStatement()

    def expression(self):
        return self.add()

    # 1 != 2
    # 2 == 2
    # if !True
    # if !someVar
    # if !hello || !bye
    # if !hey && end
    # split if into multiple tokens
    # example: if(!sayHello == True)
    # tokens = ["if", "(",  "!", "sayHello", "==", "True", ")"]
    def ifElseBlockStatement(self):

        self.advance()
        statements = []
        if self.current()['value'] == "else":
            while self.current()['type'] == "LBRACE":
                self.advance()
            statements.extend(self.blockStatement())
        else:
            while self.current()['type'] == "LPAREN":
                self.advance()
            statements.extend(self.blockStatement())
        return ast.ifElseStatement(self.statements())

    def classDeclarations(self):
        self.advance()
        className = self.current()['value']
        self.advance()
        while self.current()['type'] == "LBRACE":
            self.advance()
        methods = []
        while self.current()['type'] != "RBRACE" and self.tokens[self.index + 1]['type'] != "EOF":
            methods.extend(self.classMethods())
        self.advance()
        return ast.ClassDecl(className, methods)

    def classMethods(self):
        type = None
        if "value" in self.current() and self.current()["value"] == "static":
            type = self.current()['value']
            self.advance()

        methodName = self.current()['value']
        self.advance()
        while self.current()['type'] != "LBRACE":
            self.advance()
        self.advance()
        if self.current()['type'] != "RBRACE":
            return ast.Method(methodName, type, self.blockStatement())
        else:
            return ast.Method(methodName, type, "")

    def blockStatement(self):
        self.advance()
        statements = []
        while self.current()['type'] != "RBRACE" and self.tokens[self.index + 1]['type'] != "EOF":
            statements.extend(self.statements())
            self.advance()
        self.advance()
        return [statements]

    # Animal dog = new Animal()

    def objectCreation(self):
        className = self.current()['value']
        self.advance()
        varName = self.current()['value']
        self.advance()
        return ast.objCreation(className, varName)


# str1 = ["if", "(",  "!", "sayHello", "==", "True", ")"]
# par = Parser()
# print(par.parse(str1))
