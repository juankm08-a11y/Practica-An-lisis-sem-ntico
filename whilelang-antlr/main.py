import sys
from antlr4 import *

from WhileLangLexer import WhileLangLexer
from WhileLangParser import WhileLangParser
from semantic_visitor import SemanticVisitor

def main():
    input_stream = FileStream(sys.argv[1])

    lexer = WhileLangLexer(input_stream)
    stream = CommonTokenStream(lexer)

    parser = WhileLangParser(stream)
    tree = parser.program()

    visitor = SemanticVisitor()

    try:
        visitor.visit(tree)
        print("Programa semánticamente correcto")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()