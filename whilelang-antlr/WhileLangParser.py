# Generated from WhileLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,95,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,5,0,20,8,0,10,0,12,0,23,9,0,1,0,1,0,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,38,8,1,1,2,1,2,1,2,1,2,
        1,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,57,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,
        7,1,7,3,7,77,8,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,88,8,7,
        10,7,12,7,91,9,7,1,8,1,8,1,8,0,1,14,9,0,2,4,6,8,10,12,14,16,0,4,
        1,0,7,8,1,0,9,10,1,0,11,12,1,0,13,14,98,0,21,1,0,0,0,2,37,1,0,0,
        0,4,39,1,0,0,0,6,44,1,0,0,0,8,49,1,0,0,0,10,58,1,0,0,0,12,64,1,0,
        0,0,14,76,1,0,0,0,16,92,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,23,
        1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,
        24,25,5,0,0,1,25,1,1,0,0,0,26,27,3,4,2,0,27,28,5,1,0,0,28,38,1,0,
        0,0,29,30,3,6,3,0,30,31,5,1,0,0,31,38,1,0,0,0,32,38,3,8,4,0,33,38,
        3,10,5,0,34,38,5,15,0,0,35,36,5,16,0,0,36,38,5,1,0,0,37,26,1,0,0,
        0,37,29,1,0,0,0,37,32,1,0,0,0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,
        1,0,0,0,38,3,1,0,0,0,39,40,3,16,8,0,40,41,5,20,0,0,41,42,5,2,0,0,
        42,43,3,14,7,0,43,5,1,0,0,0,44,45,3,16,8,0,45,46,5,20,0,0,46,47,
        5,2,0,0,47,48,3,14,7,0,48,7,1,0,0,0,49,50,5,17,0,0,50,51,5,3,0,0,
        51,52,3,14,7,0,52,53,5,4,0,0,53,56,3,12,6,0,54,55,5,18,0,0,55,57,
        3,12,6,0,56,54,1,0,0,0,56,57,1,0,0,0,57,9,1,0,0,0,58,59,5,19,0,0,
        59,60,5,3,0,0,60,61,3,14,7,0,61,62,5,4,0,0,62,63,3,12,6,0,63,11,
        1,0,0,0,64,65,5,5,0,0,65,66,3,2,1,0,66,67,5,6,0,0,67,13,1,0,0,0,
        68,69,6,7,-1,0,69,77,5,21,0,0,70,77,5,22,0,0,71,77,5,20,0,0,72,73,
        5,3,0,0,73,74,3,14,7,0,74,75,5,4,0,0,75,77,1,0,0,0,76,68,1,0,0,0,
        76,70,1,0,0,0,76,71,1,0,0,0,76,72,1,0,0,0,77,89,1,0,0,0,78,79,10,
        7,0,0,79,80,7,0,0,0,80,88,3,14,7,8,81,82,10,6,0,0,82,83,7,1,0,0,
        83,88,3,14,7,7,84,85,10,5,0,0,85,86,7,2,0,0,86,88,3,14,7,6,87,78,
        1,0,0,0,87,81,1,0,0,0,87,84,1,0,0,0,88,91,1,0,0,0,89,87,1,0,0,0,
        89,90,1,0,0,0,90,15,1,0,0,0,91,89,1,0,0,0,92,93,7,3,0,0,93,17,1,
        0,0,0,6,21,37,56,76,87,89
    ]

class WhileLangParser ( Parser ):

    grammarFileName = "WhileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'('", "')'", "'{'", "'}'", 
                     "'*'", "'/'", "'+'", "'-'", "'<'", "'>'", "'int'", 
                     "'string'", "'break'", "'continue'", "'if'", "'else'", 
                     "'while'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", 
                      "IF", "ELSE", "WHILE", "ID", "INT", "STRING", "WS" ]

    RULE_programm = 0
    RULE_statement = 1
    RULE_declaration = 2
    RULE_assignment = 3
    RULE_ifStatement = 4
    RULE_whileStatement = 5
    RULE_block = 6
    RULE_expr = 7
    RULE_type = 8

    ruleNames =  [ "programm", "statement", "declaration", "assignment", 
                   "ifStatement", "whileStatement", "block", "expr", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    BREAK=15
    CONTINUE=16
    IF=17
    ELSE=18
    WHILE=19
    ID=20
    INT=21
    STRING=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgrammContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(WhileLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.StatementContext,i)


        def getRuleIndex(self):
            return WhileLangParser.RULE_programm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgramm" ):
                listener.enterProgramm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgramm" ):
                listener.exitProgramm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgramm" ):
                return visitor.visitProgramm(self)
            else:
                return visitor.visitChildren(self)




    def programm(self):

        localctx = WhileLangParser.ProgrammContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 778240) != 0):
                self.state = 18
                self.statement()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(WhileLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self):
            return self.getTypedRuleContext(WhileLangParser.DeclarationContext,0)


        def assignment(self):
            return self.getTypedRuleContext(WhileLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(WhileLangParser.IfStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(WhileLangParser.WhileStatementContext,0)


        def BREAK(self):
            return self.getToken(WhileLangParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(WhileLangParser.CONTINUE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = WhileLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 37
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.declaration()
                self.state = 27
                self.match(WhileLangParser.T__0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.assignment()
                self.state = 30
                self.match(WhileLangParser.T__0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.ifStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 33
                self.whileStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 34
                self.match(WhileLangParser.BREAK)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 35
                self.match(WhileLangParser.CONTINUE)
                self.state = 36
                self.match(WhileLangParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(WhileLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = WhileLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.type_()
            self.state = 40
            self.match(WhileLangParser.ID)
            self.state = 41
            self.match(WhileLangParser.T__1)
            self.state = 42
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(WhileLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = WhileLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.type_()
            self.state = 45
            self.match(WhileLangParser.ID)
            self.state = 46
            self.match(WhileLangParser.T__1)
            self.state = 47
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(WhileLangParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(WhileLangParser.ELSE, 0)

        def getRuleIndex(self):
            return WhileLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = WhileLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(WhileLangParser.IF)
            self.state = 50
            self.match(WhileLangParser.T__2)
            self.state = 51
            self.expr(0)
            self.state = 52
            self.match(WhileLangParser.T__3)
            self.state = 53
            self.block()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 54
                self.match(WhileLangParser.ELSE)
                self.state = 55
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(WhileLangParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(WhileLangParser.BlockContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStatement" ):
                return visitor.visitWhileStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileStatement(self):

        localctx = WhileLangParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(WhileLangParser.WHILE)
            self.state = 59
            self.match(WhileLangParser.T__2)
            self.state = 60
            self.expr(0)
            self.state = 61
            self.match(WhileLangParser.T__3)
            self.state = 62
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(WhileLangParser.StatementContext,0)


        def getRuleIndex(self):
            return WhileLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = WhileLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(WhileLangParser.T__4)
            self.state = 65
            self.statement()
            self.state = 66
            self.match(WhileLangParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(WhileLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringLiteral" ):
                listener.enterStringLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringLiteral" ):
                listener.exitStringLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringLiteral" ):
                return visitor.visitStringLiteral(self)
            else:
                return visitor.visitChildren(self)


    class VarContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(WhileLangParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class IntLiteralContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(WhileLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntLiteral" ):
                listener.enterIntLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntLiteral" ):
                listener.exitIntLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntLiteral" ):
                return visitor.visitIntLiteral(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class CompareContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompare" ):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLangParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLangParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                localctx = WhileLangParser.IntLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 69
                self.match(WhileLangParser.INT)
                pass
            elif token in [22]:
                localctx = WhileLangParser.StringLiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 70
                self.match(WhileLangParser.STRING)
                pass
            elif token in [20]:
                localctx = WhileLangParser.VarContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 71
                self.match(WhileLangParser.ID)
                pass
            elif token in [3]:
                localctx = WhileLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 72
                self.match(WhileLangParser.T__2)
                self.state = 73
                self.expr(0)
                self.state = 74
                self.match(WhileLangParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = WhileLangParser.MulDivContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 78
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 79
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 80
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = WhileLangParser.AddSubContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 81
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 82
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 83
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = WhileLangParser.CompareContext(self, WhileLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 84
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 85
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 86
                        self.expr(6)
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = WhileLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




