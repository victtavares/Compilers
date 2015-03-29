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

# file Error Constants
OPEN_ERROR = "\nERRO: Abrindo o %s\n"
CLOSE_ERROR = "\nERRO: Fechando o %s\n"


#Not Enough Arguments Error
FORMAT = "Usage: %s <arquivo1 arquivo2 ...>\n"


# Lexical Error Constants
LEXICAL_ERROR_OPEN_STRING = "String não fechada:  "
LEXICAL_ERROR_NOT_EXPECTED = "Caracter nao esperado: "

# Tipo de tokens
IDENTIFIER = "Identificador:"
INTEGER = "Inteiro:"
STRING = "Literal string:"
RESERVED = "Palavra reservada:"
END_OF_FILE = "Fim do Arquivo: %s\n\n"

# Variaveis globais

LINE = 1
POSITION = 1
CHARACTER = " "



