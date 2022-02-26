from ast import *

class Visitor:
    def visitStatements(self, asts):
        ctx = ''
        for ast in asts:
            ctx += ast.visit(self)
        return ctx

    def visitClassDecl(self, clsDecl):
        ctx = "class "
        ctx += clsDecl.clsName
        ctx += ":\n"
        methods = clsDecl.methods

        for mth in methods:
            ctx += self.visitMethod(mth, clsDecl)
        return ctx

    def visitMethod(self, method, cls):
        ctx = "\tdef "
        ctx += method.name
        if method.type != "static":
            ctx += "(self"
        else:
            ctx += "("
        if method.argument_list:
            for argument in method.argument_list:
                ctx += ", "
                ctx += argument
        ctx += "):\n"
        bodyList = method.body
        for body in bodyList:
            ctx += self.visitBody(body)
        return ctx

    def visitBody(self, body):
        ctx = ""
        if isinstance(body, ForLoopBlock):
            ctx += "\t\tfor " + body.count_name + " in range(" + body.count_value + ", "
            if body.operand == "<=" or body.operand == ">=":
                constraint = body.constraint_value + 1
                ctx += constraint
            elif body.operand == "<" or body.operand == ">":
                ctx += body.constraint_value
            ctx += ", " + body.increment + "):\n"
        elif isinstance(body, VariableAssignmentBlock):
            ctx += "\t\t" + body.var_name + " = " + body.var_value + "\n"
        elif isinstance(body, ObjCreationBlock):
            ctx += "\t\t" + body.varName + " = " + body.className + "()\n"
        elif isinstance(body, IfBlock):
            ctx += "\t\tif " + body.conditionVar + " " + body.conditionOp + " " + body.conditionVal + ":\n"
            for ifBody in body.bodyList:
                ctx += "\t" + body.visitBody(ifBody)
        elif isinstance(body, ElseBlock):
            ctx += "\t\telse:\n"
            for elseBody in body.bodyList:
                ctx += "\t" + body.visitBody(elseBody)
        elif isinstance(body, ReturnStatement):
            ctx += "\t\treturn " + body.returnString + "\n"
        return ctx
