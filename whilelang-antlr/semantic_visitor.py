from WhileLangVisitor import WhileLangVisitor
from symbol_table import SymbolTable

class SemanticVisitor(WhileLangVisitor):


    def __init__(self):
        self.symbols = SymbolTable()


    def visitDeclaration(self,ctx):

        name = ctx.ID().getText()
        type_ = ctx.type().getText()

        expr_type = self.visit(ctx.expr())

        if type != expr_type:
            raise Exception("Error: tipo incompatible en declaración.")

    
    def visitAssignment(self,ctx):

        name = ctx.ID().getText()

        var_type = self.symbols.lookup(name)
        expr_type = self.visit(ctx.expr())

        if var_type != expr_type:
            raise Exception("Error: asignación de tipo incorrecto")

    
    def visitIntLiteral(self,ctx):

        return "int"

    def visitStringLiteral(self,ctx):

        return "string"

    def visitVar(self,ctx):

        name = ctx.ID().getText()
        return self.symbols.lookup(none)

    def visitAddSub(self,ctx):

        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))

        if t1 != t2:
            raise Exception("Error: tipos incompatibles en operación")

        return t1

    def visitMulDiv(self,ctx):

        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))

        if t1 != "int" or t2 != "int":
            raise Exception("Error: operación aritmética inválida")

    def visitCompare(self,ctx):

        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))

        if t1 != t2:
            raise Exception("Error: comparación inválida.")

        return "int"

    
    def visitBlock(self,ctx):

        self.symbols.enter_scope()
        self.visitChildren(ctx)
        self.symbols.exit_scope()