# Python Import &  Modules 

Python has a way to put definitions in a file and use same in a script or in an interactive instance of the interpreter. Such a file is called a module. Definitions from a model can be imported into other modules or into the main module. 

A module is a file containing Python definitions and statements. 

>>> dir()

This functions is used to find out which names a module defines. It returns sorted list of strings.
>>> import fibo, sys
>>> dir(fibo)
 "output"
>>> dir(sys)
 "output"

# Command Line Arguments

These arguments are stored in sys module argv attribute as a list. 

# Pycodestyle

This is a tool to check python code against some of the style conventions 

# Operating Interface

The os module provides dozens of functions for interacting with the operating system.
>>> import os
>>> os.getcwd()

# File Wildcards

The module provides the function for making file lists from directory wildcard searches 
>>> import glob
>>> glob.glob('*.py')