#!/usr/bin/env python
# -*- coding: UTF-8 -*-/Users/victorTavares/Downloads/program/lexico.py
# ===============================================================================
# NOME:   Lexical.py
#
# Universidade Federal da Bahia
#    Computer Science Departament
#
#   COURSE: Compiladores
#   PROFESSOR:  Vinicius Petrucci
#   PROJECT:    Compilador de Monga 99
#   AUTHORS:    Fabio Costa <fabiomcosta@dcc.ufba.r>
#               Victor Tavares <victtavares1@gmail.com>
#
# ===============================================================================


#import sys
import Constants
#import time
#import Tokens
#from const import caracter


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



         #-------------------- LEXICAL ITEMS: State from 1/ 8 to 26 ----------------------------

        if state == 8:
            lexeme += c
            if c == "=":
                state = 9
            elif c == "+":
                state = 13
            elif c == "*":
                state = 14
            #check it here later
            elif c == "/":
                state = 15
            elif c == "%":
                state = 16
            elif c == '^':
                state = 17
            elif c == "#":
                state = 18
            elif c == "~":
                state = 19
            elif c == "<":
                state = 21
            elif c == ">":
                state = 24
            elif c == "(":
                state = 27
            elif c == ")":
                state = 28
            elif c == "{":
                state = 29
            elif c == "}":
                state = 30
            elif c == "[":
                state = 31
            elif c == "]":
                state = 32
            elif c == ";":
                state = 33
            elif c == ":":
                state = 34
            elif c == ",":
                state = 35
            elif c == ".":
                state = 36
            elif c == "\n":
                state = 41
            else:
                #Just at the final state
                if not (c == "\n" or c == ''):
                    fail(lexeme)
                state = 0

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
                print("here")
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





        # #State 12 - X = Numerical Token
        # #Initial State
        # if state == 12:
        #     #check if it's a digit 0-9
        #     if c.isdigit():
        #         lexeme += c
        #         state = 13
        #         c = nextChar(file, c)
        #     else:
        #         fail()
        #         state = 0
        #         #Last state check if c is nil
        #
        #
        # if state == 13:
        #     while True:
        #         if c.isdigit():
        #             lexeme += c
        #             c = nextChar(file, c)
        #         if not c.isdigit():
        #             state = 20
        #             break

        # if state == 20:
        #     retract()
        #     saveLexeme("Number")
        #     state = 0




        #-------------------- END OF FILE "STATE"----------------------------
        if not c:
            return Constants.TK_EOF







def saveLexeme(tokenName):
    global lexeme
    print "saving: " + tokenName + " : " + lexeme
    lexeme = ""





#Function called at the end of the automata when the generate lexeme is not valid
def fail(currentChar):
    global lexeme
    #print("The character \"" + currentChar + "\" is not a valid lexeme")
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

