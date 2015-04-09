# ===============================================================================
# NOME:   compiler.py
#
# Universidade Federal da Bahia
#   Departamento de Ciencia da Computacao
#
#   DISCIPLINA: Compiladores
#   PROFESSOR:  Vinicius Petrucci
#   PROJETO:    Lua Compiler
#   AUTORES:    Fabio Costa <fabiomcosta@dcc.ufba.r>
#               Victor Tavares <victtavares1@gmail.com>
#
# ===============================================================================


# Modules
import sys
import Constants
import Lexical


# Variables
file = ""
#TOKEN_INDEX = ""

#Argument List
arguments = sys.argv[1:]


#Test if the argument exists
if not arguments:
    print Constants.FORMAT % sys.argv[0]

for argument in arguments:
    TOKEN_INDEX = ""
    #Test if the file was open
    file = open(argument, 'r')
    if not file:
        print Constants.OPEN_ERROR % argument
        sys.exit(1)

    #While to read Mutiple files
    while TOKEN_INDEX != Constants.TK_EOF:
        TOKEN_INDEX = Lexical.searchToken(file)
        #print(TOKEN_INDEX)

    print Constants.END_OF_FILE % argument

    # Closing the file
    file.close()
    if not file.closed:
        print Constants.CLOSE_ERROR % argument
        sys.exit(1)

    # Cleaning Variables to compile the next File
    # Constants.CHARACTER = " "
    # Constants.LINE = 1
    # Constants.POSITION = 1


# End of compile
sys.exit(0)
