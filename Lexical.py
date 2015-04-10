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
lexeme = ""


#Retracted Variable - Check if a retracted had occur, if so next char will return the previous variable, not the current one
retracted = False

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
        #time.sleep(1)
        #print("--------------- Interaction " + str(state) + " ------------------")

        #Reading a character from the file if not retracted before, if so, get the last char from the buffer
        if state == 0:
            c = nextChar(file, c)
            if c == "<":
                lexeme += c
                state = 1
            elif c == "=":
                lexeme += c
                state = 5
            elif c == ">":
                lexeme += c
                state = 6
            else:
                #fail()
                state = 12


        if state == 1:
            #c = nextChar(file, c)
            if c == "=":
                lexeme += c
                state = 2
            if c == ">":
                lexeme += c
                state = 3
            else:
                lexeme += c
                state = 4

        if state == 4:
            print("Do Something later here")
        #State "="
        if state == 5:
            state = 0
            saveLexeme("Equal")


        if state == 8:
            retract()
            state = 0
            saveLexeme("Equal")




        #State 12 - X = Numerical Token
        #Initial State
        if state == 12:
            #check if it's a digit 0-9
            if c.isdigit():
                lexeme += c
                state = 13
                c = nextChar(file, c)
            else:
                fail()
                state = 0
                #Last state check if c is nil


        if state == 13:
            while True:
                if c.isdigit():
                    lexeme += c
                    c = nextChar(file, c)
                if not c.isdigit():
                    state = 20
                    break



        if state == 20:
            retract()
            saveLexeme("Number")
            state = 0





        #if Not c, it's end of file
        if not c:
            return Constants.TK_EOF






def saveLexeme(tokenName):
    global lexeme
    print tokenName
    print lexeme
    lexeme = ""





#Function called at the end of the automata when the generate lexeme is not valid
def fail():
    print("In fail Function")


#Function called to put just the readed character on the buffer and remove everything else
def retract():
    global retracted
    retracted = True


#Reading the next file
def nextChar(file,c):
    global retracted
    #if not retracted, update character, otherwise, keep the same
    if (not retracted):
        #Reading one character from the file
        c = file.readline(1)
        #print("Reading: " + c)
    else:
        #print("Returning: " + c)
        retracted = False
    return c

