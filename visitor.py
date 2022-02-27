from AbsSynTree import ClassDecl, Method, BodyBlock, ForLoopBlock, VariableAssignmentBlock, ReturnStatement, ObjCreationBlock, IfBlock, ElseBlock

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
        count = 0
        ctx = "\tdef "
        ctx += method.name
        if method.type != "static":
            ctx += "(self, "
        else:
            ctx += "("
        if method.argument_list:
            for argument in method.argument_list:
                ctx += argument
                if count < len(method.argument_list) - 1:
                    ctx += ", "
                count += 1
        ctx += "):\n"
        bodyList = method.body[0]
        for body in bodyList:
            ctx += self.visitBody(body, 0)
        return ctx

    def visitBody(self, body, level):
        ctx = ''
        if body:
            ctx += "\t\t"
            for i in range(level):
                ctx += "\t"
        if isinstance(body, ForLoopBlock):
            ctx += "for " + body.count_name + " in range(" + body.count_value + ", "
            if body.operand == "<=" or body.operand == ">=":
                constraint = body.constraint_value + 1
                ctx += constraint
            elif body.operand == "<" or body.operand == ">":
                ctx += body.constraint_value
            ctx += ", " + body.increment + "):\n"
        elif isinstance(body, VariableAssignmentBlock):
            ctx += body.var_name + " = " + body.var_value + "\n"
        elif isinstance(body, ObjCreationBlock):
            ctx += body.varName + " = " + body.className + "()\n"
        elif isinstance(body, IfBlock):
            ctx += "if " + body.conditionVar + " " + body.conditionOp + " " + body.conditionVal + ":\n"
            for ifBody in body.bodyList:
                ctx += self.visitBody(ifBody, level + 1)
        elif isinstance(body, ElseBlock):
            ctx += "else:\n"
            for elseBody in body.bodyList:
                ctx += self.visitBody(elseBody, level + 1)
        elif isinstance(body, ReturnStatement):
            if body.returnMethodName:
                count = 0
                ctx += body.returnString + " " + body.returnMethodName + "("
                for argument in body.returnMethodArgList:
                    ctx += argument
                    if count < len(body.returnMethodArgList) - 1:
                        ctx += ", "
                    count += 1
                ctx += ")\n"
            else:
                ctx += body.returnString + " " + body.returnVal + "\n"
        return ctx
