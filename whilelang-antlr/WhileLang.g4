grammar WhileLang;

programm: statement* EOF;

statement
    : declaration ';'
    | assignment ';'
    | ifStatement
    | whileStatement
    | BREAK
    | CONTINUE ';'
    ;

declaration 
    : type ID '=' expr
    ;

assignment
    : type ID '=' expr
    ;

ifStatement
    : IF '(' expr ')' block (ELSE block)?
    ;

whileStatement
    : WHILE '('expr')' block
    ;

block
    : '{' statement '}'
    ;


expr
    : expr op=('*'|'/') expr #mulDiv
    | expr op=('+'|'-') expr #addSub
    | expr op=('<'|'>') expr #Compare
    | INT               # IntLiteral
    | STRING            # StringLiteral
    | ID                # Var
    | '('expr')'        # Parens 
    ;

type
    : 'int'
    | 'string'
    ;

BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
WHILE: 'while';

ID: [a-zA-Z_][a-zA-Z0-9_]*;
INT: [0-9]+;
STRING: '"' .*?  '"';

WS: [ \t\r\n]+ -> skip;