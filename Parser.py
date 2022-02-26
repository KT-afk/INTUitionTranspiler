from contextlib import nullcontext
import this
from ast import ClassDecl, Method, objCreation, ifElseStatement, forLoopBlock, variableAssignmentBlock


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
            self.expr.append(self.statements())
        return self.expr

    def statements(self):
        current = self.current()
        next = self.peep()
        if "value" in self.tokens[self.index]:
            if current['value'] == "class":
                return self.classDeclarations()
            elif "value" in self.tokens[self.index + 3] and self.tokens[self.index + 3]['value'] == "new":
                return self.objectCreation()
            elif current['value'] == "if" or current['value'] == "else":
                return self.ifElseBlockStatement()
            elif current['value'] == "for" or current['value'] == "while":
                return self.forLoop()
            elif current['type'] == "IDENTIFIER" and next['value'] == "=":
                return self.variableAssignment()
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
        return ifElseStatement(self.statements())

    def variableAssignment(self):
        varName = self.current()['value']
        self.advance()
        self.advance()
        varValue = self.current()['value']
        return variableAssignmentBlock(varName, varValue)

    def forLoop(self):
        while self.current()['type'] != "IDENTIFIER":
            self.advance()
        count_name = self.current()['value']
        while self.current()['type'] != "NUM":
            self.advance()
        count_value = self.current()['value']

        while self.current()['type'] != "OP":
            self.advance()
        operand = self.current()['value']
        self.advance()
        constraint_value = self.current()['value']
        while self.current()['type'] != "OP":
            self.advance()
        increment = self.current()['value']
        while self.current()['type'] != "EOF":
            self.advance()
        self.advance()
        return forLoopBlock(count_name, count_value, operand, constraint_value, increment)
    #while(i < 10){
    #   i += 1
    # }
    def whileLoop(self):
        while self.current()['type'] != "IDENTIFIER":
            self.advance()
        count_name = self.current()['value']
        while self.current()['type'] != "NUM":
            self.advance()
        count_value = self.current()['value']

        while self.current()['type'] != "OP":
            self.advance()
        operand = self.current()['value']
        self.advance()
        constraint_value = self.current()['value']
        while self.current()['type'] != "OP":
            self.advance()
        increment = self.current()['value']
        while self.current()['type'] != "EOF":
            self.advance()
        self.advance()
        return forLoopBlock(count_name, count_value, operand, constraint_value, increment)
    def classDeclarations(self):
        self.advance()
        className = self.current()['value']
        self.advance()
        while self.current()['type'] == "LBRACE":
            self.advance()
        methods = []
        while self.current()['type'] != "RBRACE" and self.tokens[self.index + 1]['type'] != "EOF":
            methods.append(self.classMethods())
        self.advance()
        return ClassDecl(className, methods)

    def classMethods(self):
        typeOfMethod = None
        if "value" in self.current() and self.current()["value"] == "static":
            typeOfMethod = self.current()['value']
            self.advance()

        methodName = self.current()['value']
        self.advance()
        while self.current()['type'] != "LBRACE":
            self.advance()
        self.advance()
        if self.current()['type'] != "RBRACE":
            return Method(methodName, typeOfMethod, self.blockStatement())
        else:
            self.advance()
            return Method(methodName, typeOfMethod, [])

    def blockStatement(self):
        self.advance()
        statements = []
        while self.current()['type'] != "RBRACE" and self.tokens[self.index + 1]['type'] != "EOF":
            statements.append(self.statements())
            self.advance()
        self.advance()
        return [statements]

    # Animal dog = new Animal()

    def objectCreation(self):
        className = self.current()['value']
        self.advance()
        varName = self.current()['value']
        self.advance()
        return objCreation(className, varName)


# str1 = ["if", "(",  "!", "sayHello", "==", "True", ")"]
# par = Parser()
# print(par.parse(str1))
