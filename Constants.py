# ===============================================================================
#   NOME:   Constants.py
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
TK_EOF = "TK_Eof"
TK_AND = "TK_And"

    # 'TK_And': 'and', 'TK_Do': 'do', 'TK_Else': 'else', 'TK_If': 'if',
    # 'TK_Int': 'int', 'TK_New': 'new', 'TK_Nil': 'nil', 'TK_Not': 'not',
    # 'TK_Or': 'or', 'TK_Return': 'return', 'TK_String': 'string',
    # 'TK_Then': 'then', 'TK_Void': 'void', 'TK_While': 'while', 'TK_Eof': '',
    # 'TK_PtoVg': ';', 'TK_Virg': ',', 'TK_AbrCol': '[', 'TK_FecCol': ']',
    # 'TK_AbrPar': '(', 'TK_FecPar': ')', 'TK_AbrCh': '{', 'TK_FecCh': '}',
    # 'TK_Soma': '+', 'TK_Menos': '-', 'TK_Divide': '/', 'TK_Mult': '*',
    # 'TK_Atrib': '=', 'TK_Menor': '<', 'TK_Maior': '>', 'TK_IgIg': '==',
    # 'TK_MenIg': '<=', 'TK_MaiIg': '>=', 'TK_Numero': '', 'TK_Cadeia': '',
    # 'TK_Iden': ''




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



