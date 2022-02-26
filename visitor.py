from ast import ClassDecl, Method, objCreation

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
        ctx += "():\n"
        #body = method.body
        return ctx
