# Generated from WhileLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .WhileLangParser import WhileLangParser
else:
    from WhileLangParser import WhileLangParser

# This class defines a complete listener for a parse tree produced by WhileLangParser.
class WhileLangListener(ParseTreeListener):

    # Enter a parse tree produced by WhileLangParser#programm.
    def enterProgramm(self, ctx:WhileLangParser.ProgrammContext):
        pass

    # Exit a parse tree produced by WhileLangParser#programm.
    def exitProgramm(self, ctx:WhileLangParser.ProgrammContext):
        pass


    # Enter a parse tree produced by WhileLangParser#statement.
    def enterStatement(self, ctx:WhileLangParser.StatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#statement.
    def exitStatement(self, ctx:WhileLangParser.StatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#declaration.
    def enterDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by WhileLangParser#declaration.
    def exitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by WhileLangParser#assignment.
    def enterAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by WhileLangParser#assignment.
    def exitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by WhileLangParser#ifStatement.
    def enterIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#ifStatement.
    def exitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#whileStatement.
    def enterWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by WhileLangParser#whileStatement.
    def exitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by WhileLangParser#block.
    def enterBlock(self, ctx:WhileLangParser.BlockContext):
        pass

    # Exit a parse tree produced by WhileLangParser#block.
    def exitBlock(self, ctx:WhileLangParser.BlockContext):
        pass


    # Enter a parse tree produced by WhileLangParser#StringLiteral.
    def enterStringLiteral(self, ctx:WhileLangParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by WhileLangParser#StringLiteral.
    def exitStringLiteral(self, ctx:WhileLangParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Var.
    def enterVar(self, ctx:WhileLangParser.VarContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Var.
    def exitVar(self, ctx:WhileLangParser.VarContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Parens.
    def enterParens(self, ctx:WhileLangParser.ParensContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Parens.
    def exitParens(self, ctx:WhileLangParser.ParensContext):
        pass


    # Enter a parse tree produced by WhileLangParser#IntLiteral.
    def enterIntLiteral(self, ctx:WhileLangParser.IntLiteralContext):
        pass

    # Exit a parse tree produced by WhileLangParser#IntLiteral.
    def exitIntLiteral(self, ctx:WhileLangParser.IntLiteralContext):
        pass


    # Enter a parse tree produced by WhileLangParser#addSub.
    def enterAddSub(self, ctx:WhileLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by WhileLangParser#addSub.
    def exitAddSub(self, ctx:WhileLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by WhileLangParser#Compare.
    def enterCompare(self, ctx:WhileLangParser.CompareContext):
        pass

    # Exit a parse tree produced by WhileLangParser#Compare.
    def exitCompare(self, ctx:WhileLangParser.CompareContext):
        pass


    # Enter a parse tree produced by WhileLangParser#mulDiv.
    def enterMulDiv(self, ctx:WhileLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by WhileLangParser#mulDiv.
    def exitMulDiv(self, ctx:WhileLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by WhileLangParser#type.
    def enterType(self, ctx:WhileLangParser.TypeContext):
        pass

    # Exit a parse tree produced by WhileLangParser#type.
    def exitType(self, ctx:WhileLangParser.TypeContext):
        pass



del WhileLangParser