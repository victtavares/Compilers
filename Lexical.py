#!/usr/bin/env python
# -*- coding: UTF-8 -*-/Users/victorTavares/Downloads/program/lexico.py
# ===============================================================================
#   NOME:   Lexical.py
#
#   Universidade Federal da Bahia
#   Departamento de Ciencia da Computacao
#
#   DISCIPLINA: Compiladores
#   PROFESSOR:  Vinicius Petrucci
#   PROJETO:    Compilador de Monga 99
#   AUTORES:    Fabio Costa <fabiomcosta@dcc.ufba.r>
#               Victor Tavares <victtavares1@gmail.com>
#
# ===============================================================================


import sys
import Constants
#from const import caracter

# Debug 1 = on // 0 = off
DEBUG = 0

#Lexical Variables
TOKEN_NAME = ""
TOKEN_TYPE = ""

def searchToken(file):
    print "Search token"
