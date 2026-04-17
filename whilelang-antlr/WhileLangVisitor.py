# Generated from WhileLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete generic visitor for a parse tree produced by WhileLangParser.

class WhileLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by WhileLangParser#programm.
    def visitProgramm(self, ctx:WhileLangParser.ProgrammContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#statement.
    def visitStatement(self, ctx:WhileLangParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#declaration.
    def visitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#assignment.
    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#ifStatement.
    def visitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#whileStatement.
    def visitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#block.
    def visitBlock(self, ctx:WhileLangParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#StringLiteral.
    def visitStringLiteral(self, ctx:WhileLangParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#Var.
    def visitVar(self, ctx:WhileLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#Parens.
    def visitParens(self, ctx:WhileLangParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#IntLiteral.
    def visitIntLiteral(self, ctx:WhileLangParser.IntLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#addSub.
    def visitAddSub(self, ctx:WhileLangParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#Compare.
    def visitCompare(self, ctx:WhileLangParser.CompareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#mulDiv.
    def visitMulDiv(self, ctx:WhileLangParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by WhileLangParser#type.
    def visitType(self, ctx:WhileLangParser.TypeContext):
        return self.visitChildren(ctx)



del WhileLangParser