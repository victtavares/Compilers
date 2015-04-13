#!/usr/bin/env python
# ===============================================================================
# NOME:   Lexical.py
#
# Universidade Federal da Bahia
#    Computer Science Departament
#
#   COURSE:     Compilers
#   PROFESSOR:  Vinicius Petrucci
#   PROJECT:    Lua Compiler
#   AUTHORS:    Fabio Costa <fabiomcosta@dcc.ufba.r>
#               Victor Tavares <victtavares1@gmail.com>
#
# ===============================================================================


#import sys
import Constants
#import time
#import Tokens


#Lexical Variables
lexeme = ""


#Retracted Variable - Check if a retracted had occur, if so next char will return the previous variable, not the current one
retracted = False

#automato state - Current position on the determinist automata
state = 0
c = ""


def searchToken(file):
    global state
    global lexeme
    global retracted
    global c
    # The next transition, will be -1 if there's no next transition
    #Do while c is not a end of file token - infinite loop
    while True:

        #-------------------- COMMENTARIES: State from 0 to 7 ----------------------------

        #Reading a character from the file if not retracted before, if so, get the last char from the buffer
        if state == 0:
            #print("state 0")
            c = nextChar(file)
            if c == "-":
                lexeme += c
                state = 1
            else:
                state = 8


        #Comment "-"
        if state == 1:
            c = nextChar(file)
            if c == "-":
                lexeme += c
                state = 2
            else:
                state = 12

        #Comment: "--"
        if state == 2:
            c = nextChar(file)
            if c == "[":
                lexeme += c
                state = 3
            elif c == "\n":
                state = 6
            else:
                lexeme +=c
                state = 4

        #Comment: "--["
        if state == 3:
            while True:
                c = nextChar(file)
                if c == "]":
                    lexeme += c
                    state = 7
                    break
                elif not c:
                    fail(lexeme)
                    break
                else:
                    lexeme += c

        #CommentOneline -  #--* where * is something different from [ or end of line
        if state == 4:

            while True:
                #print ("whiletrue state 4")
                c = nextChar(file)
                # end of line or end of file
                if c == '\n' or not c:
                    lexeme += c
                    state = 5
                    break
                else:
                    lexeme += c

        #Final state - Comment one line
        if state == 5:
            saveLexeme("OneLine Comment")
            state = 0
            break

        #Final state - Just -- with no text
        if state == 6:
            saveLexeme("OneLine Comment")




        #Final State - Comment: "--[*" where * can be a string of characters
        if state == 7:
            saveLexeme("Comment")
            state = 0
            break



         #-------------------- LEXICAL ITEMS: State from 1/ 8 to 41 ----------------------------

        if state == 8:
            #
            if c == "=":
                lexeme += c
                state = 9
            elif c == "+":
                lexeme += c
                state = 13
            elif c == "*":
                lexeme += c
                state = 14
            #check it here later
            elif c == "/":
                lexeme += c
                state = 15
            elif c == "%":
                lexeme += c
                state = 16
            elif c == '^':
                lexeme += c
                state = 17
            elif c == "#":
                lexeme += c
                state = 18
            elif c == "~":
                lexeme += c
                state = 19
            elif c == "<":
                lexeme += c
                state = 21
            elif c == ">":
                lexeme += c
                state = 24
            elif c == "(":
                lexeme += c
                state = 27
            elif c == ")":
                lexeme += c
                state = 28
            elif c == "{":
                lexeme += c
                state = 29
            elif c == "}":
                lexeme += c
                state = 30
            elif c == "[":
                lexeme += c
                state = 31
            elif c == "]":
                lexeme += c
                state = 32
            elif c == ";":
                lexeme += c
                state = 33
            elif c == ":":
                lexeme += c
                state = 34
            elif c == ",":
                lexeme += c
                state = 35
            elif c == ".":
                lexeme += c
                state = 36
            elif c == "\n":
                lexeme += c
                state = 41
            else:
                state = 42

        #Check the =
        if state == 9:
            c = nextChar(file)
            if c == "=":
                lexeme += c
                state = 11
            else:
                state = 10

        # Final State =
        if state == 10:
            retract()
            saveLexeme(Constants.TK_EQUAL)
            state = 0
            break

        #Final State  ==
        if state == 11:
            saveLexeme(Constants.TK_COMPARISON)
            state = 0
            break

        #Final State -
        if state == 12:
            retract()
            saveLexeme(Constants.TK_MINUS)
            state = 0
            break

        #Final State +
        if state == 13:
            saveLexeme(Constants.TK_PLUS)
            state = 0
            break

        #Final State *
        if state == 14:
            saveLexeme(Constants.TK_MULTI)
            state = 0
            break

        #Final State /
        if state == 15:
            saveLexeme(Constants.TK_DIV)
            state = 0
            break

        #Final State %
        if state == 16:
            saveLexeme(Constants.TK_MOD)
            state = 0
            break

        #Final State ^
        if state == 17:
            saveLexeme(Constants.TK_DIV)
            state = 0
            break

         #Final State #
        if state == 18:
            saveLexeme(Constants.TK_HASH)
            state = 0
            break

        #Check the ~
        if state == 19:
            c = nextChar(file)
            if (c == "="):
                lexeme += c
                state = 20
            else:
                fail(lexeme)
                state = 0
                break

        if state == 20:
            saveLexeme(Constants.TK_TILDE_EQUAL)
            state = 0
            break

        #Check the <
        if state == 21:
            c = nextChar(file)
            if c == "=":
                lexeme += c
                state = 23
            else:
                state = 22

        # Final State <
        if state == 22:
            retract()
            saveLexeme(Constants.TK_LESS_THAN)
            state = 0
            break

        #Final State  <=
        if state == 23:
            saveLexeme(Constants.TK_LESS_EQ)
            state = 0
            break


        #Check the >
        if state == 24:
            c = nextChar(file)
            if c == "=":
                lexeme += c
                state = 26
            else:
                state = 25

        # Final State >
        if state == 25:
            retract()
            saveLexeme(Constants.TK__BIGGER_THAN)
            state = 0
            break

        #Final State  >=
        if state == 26:
            saveLexeme(Constants.TK_BIGGER_EQ)
            state = 0
            break


        #Final State (
        if state == 27:
            saveLexeme(Constants.TK_OPEN_PAREN)
            state = 0
            break

        #Final State )
        if state == 28:
            saveLexeme(Constants.TK_CLOSE_PAREN)
            state = 0
            break

        #Final State {
        if state == 29:
            saveLexeme(Constants.TK_OPEN_BRACE)
            state = 0
            break

        #Final State }
        if state == 30:
            saveLexeme(Constants.TK_CLOSE_BRACE)
            state = 0
            break

        #Final State [
        if state == 31:
            saveLexeme(Constants.TK_OPEN_BRACKET)
            state = 0
            break

        #Final State ]
        if state == 32:
            saveLexeme(Constants.TK_CLOSE_BRACKET)
            state = 0
            break

        #Final State ;
        if state == 33:
            saveLexeme(Constants.TK_SEMICOLON)
            state = 0
            break

        #Final State :
        if state == 34:
            saveLexeme(Constants.TK_COLON)
            state = 0
            break

        #Final State ,
        if state == 35:
            saveLexeme(Constants.TK_COMMA)
            state = 0
            break


        #Check the .
        if state == 36:
            c = nextChar(file)
            if c == ".":
                lexeme += c
                state = 38
            else:
                state = 37

        # Final State .
        if state == 37:
            retract()
            saveLexeme(Constants.TK_DOT)
            state = 0
            break

        #Check the ..
        if state == 38:
            c = nextChar(file)
            if c == ".":
                lexeme += c
                state = 40
            else:
                state = 39

        #Final State ..
        if state == 39:
            retract()
            saveLexeme(Constants.TK_TWO_DOTS)
            state = 0

        #Final State ...
        if state == 40:
            saveLexeme(Constants.TK_THREE_DOTS)
            state = 0

        #Final State \n
        if state == 41:
            saveLexeme(Constants.TK_END_OF_LINE)
            state = 0
            break



         #-------------------- IDENTIFIERS: State from 42 to 44 ----------------------------
        #Reading alpha or _
        if state == 42:
            if c.isalpha() or c == "_":
                lexeme += c
                #print("Inside c.isalpha - lexeme on state 42:" + lexeme + " and c:" + c)
                state = 43
            else:
                state = 45
        #Alpha or _ followed by a sequence of alpha, number and _
        if state == 43:
            while True:
                c = nextChar(file)
                if c.isalpha() or c.isdigit() or c == "_":
                    lexeme += c
                    #print("Inside c.isalpha - lexeme on state 43:" + lexeme + " and c:" + c)
                else:
                    state = 44
                    break

        if state == 44:
            retract()
            identifier = isKeyword()
            saveLexeme(identifier)
            state = 0
            break


        #-------------------- DELIMITERS: State from 45 to 47 ----------------------------
        #Reading DELIM
        if state == 45:
            if c == " ":
                state = 46
            else:
                state = 48

        #DELIM
        if state == 46:
            while True:
                c = nextChar(file)
                if c != " ":
                    state = 47
                    break

        #DELIM Final state
        if state == 47:
            retract()
            state = 0
            break


        #-------------------- Number: State from 48 to 60 ----------------------------
        #Reading a number char
        if state == 48:
            #print(lexeme + " on state 48")
            if c == "0":
                lexeme += c
                state = 50
            elif c.isdigit():
                lexeme += c
                state = 49
            else:
                state = 61

        #Reading a digit, not 0
        if state == 49:
            while True:
                c = nextChar(file)
                if c.isdigit():
                    lexeme += c
                elif c == ".":
                    lexeme += c
                    #print(lexeme + " on state 49")
                    state = 54
                    break
                elif c.lower() == "e":
                    lexeme += c
                    state = 57
                    break
                else:
                    state = 53
                    break

        #Reading 0
        if state == 50:
            c = nextChar(file)
            lexeme += c
            #print(lexeme + " on state 50")
            if c.lower() == "x":
                state = 51
            elif c.isdigit():
                state = 49
            elif c == ".":
                state = 54
            else:
                state = 53


        #Reading 0x
        if state == 51:
            while True:
                c = nextChar(file)
                if c.lower() in ["a","b","c","d","e","f"] or c.isdigit():
                    lexeme += c
                else:
                    state = 52
                    break

        #Final state - Hexadecimal 0x....
        if state == 52:
            retract()
            saveLexeme(Constants.TK_NUMBER_HEX)
            state = 0
            break

        #Final state - Number 01212- int
        if state == 53:
            retract()
            saveLexeme(Constants.TK_NUMBER_INT)
            state = 0
            break

        #Reading digits + "."
        if state == 54:
            c = nextChar(file)
            if c.isdigit():
                lexeme += c
                state = 55
            else:
                fail(lexeme)
                state = 0
                break
        #Reading digits + "." + digits
        if state == 55:
            while True:
                c = nextChar(file)
                if c.isdigit():
                    lexeme += c
                elif c.lower() == "e":
                    lexeme += c
                    state = 57
                    break
                else:
                    state = 56
                    break

        #Final State - digits + "." + digits
        if state == 56:
            retract()
            saveLexeme(Constants.TK_NUMBER_FLOAT)
            state = 0
            break

        #Reading number + e + "+" or "-"
        if state == 57:
            c = nextChar(file)
            if c in ["+","-"]:
                lexeme += c
                state = 58
            elif c.isdigit():
                lexeme += c
                state = 59
            else:
                fail(lexeme)
                state = 0
                break

        if state == 58:
            c = nextChar(file)

            if c.isdigit():
                lexeme += c
                state = 59
            else:
                fail(lexeme)
                state = 0
                break

        if state == 59:
            while True:
                c = nextChar(file)
                if c.isdigit():
                    lexeme += c
                else:
                    state = 60
                    break

        if state == 60:
            retract()
            saveLexeme(Constants.TK_NUMBER_EXPO)
            state = 0
            break



        #-------------------- Literal String: State from 61 to 70 ----------------------------
        #Reading a string literal
        if state == 61:
            if c == '"':
                lexeme += c
                state = 62
            else:
                state = 66
        #Reading "
        if state == 62:
            while True:
                c = nextChar(file)
                if c == '"':
                    lexeme += c
                    state = 63
                    break
                elif c == '\\':
                    lexeme += c
                    state = 64
                    break
                elif c == "\n" or c == "":
                    fail(lexeme)
                    state = 0
                    break
                else:
                    lexeme += c
        #Reading "......"
        if state == 63:
            saveLexeme(Constants.TK_STRING_LITERAL)
            state = 0
            break

        #Reading ".....\...."
        if state == 64:
            c = nextChar(file)

            if c == '"':
                lexeme += c
                state = 65
            elif c == "\n" or c == "":
                    fail(lexeme)
                    state = 0
                    break
            else:
                lexeme += c
                state = 62
                break

        if state == 65:
            while True:
                #print("state 65:" + lexeme + " with c:" + c)
                c = nextChar(file)
                if c == '"':
                    lexeme += c
                    state = 63
                    break
                elif c == '\\':
                    lexeme += c
                    state = 64
                    break
                elif c == "\n" or c == "":
                    fail(lexeme)
                    state = 0
                    break
                else:
                    lexeme += c












        if state == 66:
            if c == "'":
                state = 67
                lexeme += c
            else:
                #Just at the final state
                if not (c == "\n" or c == ''):
                    fail(lexeme)
                state = 0



         #Reading '
        if state == 67:
            while True:
                c = nextChar(file)
                if c == "'":
                    lexeme += c
                    state = 68
                    break
                elif c == '\\':
                    lexeme += c
                    state = 69
                    break
                elif c == "\n" or c == "":
                    fail(lexeme)
                    state = 0
                    break
                else:
                    lexeme += c

        #Reading '......'
        if state == 68:
            saveLexeme(Constants.TK_STRING_LITERAL)
            state = 0
            break

        #Reading '.....\....'
        if state == 69:
            c = nextChar(file)

            if c == "'":
                lexeme += c
                state = 70
            elif c == "\n" or c == "":
                    fail(lexeme)
                    state = 0
                    break
            else:
                lexeme += c
                state = 67
                break

        if state == 70:
            while True:
                c = nextChar(file)
                if c == "'":
                    lexeme += c
                    state = 68
                    break
                elif c == '\\':
                    lexeme += c
                    state = 69
                    break
                elif c == "\n" or c == "":
                    fail(lexeme)
                    state = 0
                    break
                else:
                    lexeme += c





        #-------------------- END OF FILE "STATE"----------------------------
        if not c:
            return Constants.TK_EOF





def isKeyword():
    global lexeme
    if lexeme in Constants.myKeywords.keys():
        return Constants.myKeywords[lexeme]
    else:
        return Constants.TK_IDENTIFIER




def saveLexeme(tokenName):
    global lexeme
    print "saving: " + tokenName + " : " + lexeme
    lexeme = ""





#Function called at the end of the automata when the generate lexeme is not valid
def fail(currentChar):
    global lexeme
    print("The character(s) \"" + currentChar + "\" is not a valid lexeme")
    lexeme = ""



#Function called to put just the readed character on the buffer and remove everything else
def retract():
    #print("retract")
    global retracted
    retracted = True


#Reading the next file
def nextChar(file):
    global c
    #time.sleep(1)
    global retracted
    #if not retracted, update character, otherwise, keep the same
    if not retracted:
        #Reading one character from the file
        c = file.readline(1)
        #print("Reading: " + c)
    else:
        #print("Returning: " + c)
        retracted = False
    return c

