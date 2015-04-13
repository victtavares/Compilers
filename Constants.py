# ===============================================================================
# NOME:   Constants.py
#
#   Federal University of Bahia
#   Computer Science Departament
#
#   COURSE: Compilers
#   PROFESSOR:  Vinicius Petrucci
#   PROJECT:    Lua Compiler
#   AUTHORS:    Fabio Costa <fabiomcosta@dcc.ufba.r>
#               Victor Tavares <victtavares1@gmail.com>
#
# ===============================================================================

#Token Keys and
TK_EOF = "TK_EOF"
TK_AND = "TK_AND"  # and

#Tokens - Lexical Keys
TK_EQUAL = "TK_EQUAL"  #
TK_MINUS = "TK_MINUS"  #-
TK_COMPARISON = "TK_COMPARISON"  # ==
TK_PLUS = "TK_PLUS"  # +
TK_MULTI = "TK_MULTI"  # *
TK_DIV = "TK_DIV"  # \
TK_MOD = "TK_MOD"  # %
TK_PON = "TK_PON"  # ^
TK_HASH = "TK_HASH"  # #
TK_TILDE_EQUAL = "TK_TILDE_EQUAL"  #=
TK_LESS_EQ = "TK_LESS_EQ"  # <=
TK_LESS_THAN = "TK_LESS_THAN"  # <
TK_BIGGER_EQ = "TK_BIGGER_EQ"  # >=
TK__BIGGER_THAN = "TK_BIGGER_THAN"  # >
TK_OPEN_PAREN = "TK_OPEN_PAREN"  # (
TK_CLOSE_PAREN = "TK_CLOSE_PAREN"  # )
TK_OPEN_BRACE = "TK_OPEN_BRACE"  # {
TK_CLOSE_BRACE = "TK_CLOSE_BRACE"  # }
TK_OPEN_BRACKET = "TK_OPEN_BRACKET"  # [
TK_CLOSE_BRACKET = "TK_CLOSE_BRACKET"  # ]
TK_SEMICOLON = "TK_SEMICOLON"  #;
TK_COLON = "TK_COLON"  #:
TK_COMMA = "TK_COMMA"  #,
TK_DOT = "TK_DOT"  #.
TK_TWO_DOTS = "TK_TWO_DOTS"  #..
TK_THREE_DOTS = "TK_THREE_DOTS"  #...
TK_END_OF_LINE = "TK_END_OF_LINE"  #\n


#Tokens - Identifier
TK_IDENTIFIER = "TK_IDENTIFIER"
myKeywords = {"and": 'TK_AND', 'break': 'TK_BREAK', 'do': 'TK_DO', 'else': 'TK_ELSE', 'elseif': 'TK_ELSEIF'
    ,"end": "TK_END", "false": "TK_FALSE", "for": "TK_FOR", "function": "TK_FUNCTION", "if": "TK_IF",
              "in": "TK_IN", "local": "TK_LOCAL", "nil": "TK_NIL", "not": "TK_NOT", "or": "TK_OR",
              "repeat": "TK_REPEAT", "return": "TK_RETURN", "then": "TK_THEN", "true": "TK_TRUE", "until": "TK_UNTIL",
              "while": "TK_WHILE"}
# TK_AND = "TK_AND"
# TK_BREAK = "TK_BREAK"
# TK_DO = "TK_DO"
# TK_ELSE = "TK_ELSE"
# TK_ELSEIF = "TK_ELSEIF"
# TK_END = "TK_END"
# TK_FALSE = "TK_FALSE"
# TK_FOR = "TK_FOR"
# TK_FUNCTION = "TK_FUNCTION"
# TK_IF = "TK_IF"
# TK_IN = "TK_IN"
# TK_LOCAL = "TK_LOCAL"
# TK_NIL = "TK_NIL"
# TK_NOT = "TK_NOT"
# TK_OR = "TK_OR"
# TK_REPEAT = "TK_REPEAT"
# TK_RETURN = "TK_RETURN"
# TK_THEN = "TK_THEN"
# TK_TRUE = "TK_TRUE"
# TK_UNTIL = "TK_UNTIL"
# TK_WHILE = "TK_WHILE"

#Tokens - Numbers
TK_NUMBER_HEX = "TK_NUMBER_HEX"
TK_NUMBER_INT = "TK_NUMBER_INT"
TK_NUMBER_FLOAT = "TK_NUMBER_FLOAT"
TK_NUMBER_EXPO = "TK_NUMBER_EXPO"


#String Literal
TK_STRING_LITERAL = "TK_STRING_LITERAL"






# file Error Constants
OPEN_ERROR = "\nERRO: Abrindo o %s\n"
CLOSE_ERROR = "\nERRO: Fechando o %s\n"


#Not Enough Arguments Error
FORMAT = "Usage: %s <arquivo1 arquivo2 ...>\n"


# Lexical Error Constants
LEXICAL_ERROR_OPEN_STRING = "String nao fechada: "
LEXICAL_ERROR_NOT_EXPECTED = "Caracter nao esperado: "

# Tipo de tokens
IDENTIFIER = "Identificador:"
INTEGER = "Inteiro:"
STRING = "Literal string:"
RESERVED = "Palavra reservada:"
END_OF_FILE = "Fim do Arquivo: %s\n"

# Variaveis globais

# LINE = 1
# POSITION = 1
# CHARACTER = " "



