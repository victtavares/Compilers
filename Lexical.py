#!/usr/bin/env python
# -*- coding: UTF-8 -*-/Users/victorTavares/Downloads/program/lexico.py
# ===============================================================================
# NOME:   Lexical.py
#
# Universidade Federal da Bahia
#   Departamento de Ciencia da Computacao
#
#   DISCIPLINA: Compiladores
#   PROFESSOR:  Vinicius Petrucci
#   PROJETO:    Compilador de Monga 99
#   AUTORES:    Fabio Costa <fabiomcosta@dcc.ufba.r>
#               Victor Tavares <victtavares1@gmail.com>
#
# ===============================================================================


#import sys
import Constants
import time
#import Tokens
#from const import caracter


#Lexical Variables
myBuffer = ""
lexeme = ""
currentIndex = -1
TOKEN_TYPE = ""


#Retracted Variable - Check if a retracted had occur, if so next char will return the previous variable, not the current one
retracted = False
previousChar = ""
currentChar = ""
#automato state => Current position on the automato
state = 0


def searchToken(file):
    global state
    global lexeme
    global retracted
    c = ""
    # The next transition, will be -1 if there's no next transition
    #Do while c is not a end of file token - infinite loop
    while True:
        time.sleep(1)
        print("--------------- Interaction " + str(state) + " ------------------")

        #Reading a character from the file if not retracted before, if so, get the last char from the buffer
        if retracted:
            length = len(myBuffer)
            c = myBuffer
            print("After retracted:" + c)
            retracted = False
        else:
            c = nextChar(file)

        #State 1 -- 9 = relop characters
        #Initial State for Special Character: >, = and <
        if state == 0:
            if c == "<":
                state = 1
            elif c == "=":
                state = 5
            elif c == ">":
                state = 6
            else:
                #fail()
                state = 12
                break

        if state == 1:
            c = nextChar(file)
            if c == "=":
                state = 2
            if c == ">":
                state = 3
            else:
                state = 4

        if state == 4:
            print("Do Something later here")
        #State "="
        if state == 5:
            state = 0
            lexeme = myBuffer
            saveLexeme("Equal", lexeme)
            clearBuffer()
            break

        if state == 8:
            retract()
            state = 0
            saveLexeme("Equal", lexeme)

            break


        #State 12 - X = Numerical Token
        #Initial State
        if state == 12:
            #check if it's a digit 0-9
            if c.isdigit():
                state = 13
            else:
                fail()
                #Last state check if c is nil
                if not c:
                    print("Not c")
                    return Constants.TK_EOF
            break


        if state == 13:
            while True:
                #c = nextChar(file)
                if not c.isdigit():
                    retract()
                    saveLexeme("Number", lexeme)
                    state = 0
                break
            break


        #if Not c, it's end of file






def saveLexeme(tokenName, lexeme):
    print tokenName
    print lexeme



def clearBuffer():
    global myBuffer
    global currentIndex

    myBuffer = ""
    currentIndex = -1

#Function called at the end of the automata when the generate lexeme is not valid
def fail():
    #Global variables
    #global state
    global myBuffer
    global currentIndex

    print("In fail Function")
    #Restarting the buffer, not a valid character
    myBuffer = ""
    currentIndex = -1


#Function called to put just the readed character on the buffer and remove everything else
def retract():
    global state
    global myBuffer
    global currentIndex
    global retracted, lexeme

    #Lexeme is everything before
    length = len(myBuffer)
    lexeme = myBuffer[0:length-1]
    #setting the state to the beginning
    state = 0
    #Remove the rest of the buffer and start with new character

    myBuffer = myBuffer[length - 1]
    currentIndex = 0
    retracted = True
    print "Buffer on retract: " + myBuffer



#Reading the next file
def nextChar(file):
    global myBuffer
    global currentIndex
    #Reading one character from the file
    c = file.readline(1)
    print("Reading: " + c)
    #c will return null in case of a end of file
    if c:
        myBuffer += c
        currentIndex += 1
        return myBuffer[currentIndex]
    else:
        return c
    #Returning the read character
