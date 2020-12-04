#!/usr/bin/env python3 -tt
#-*- coding: UTF-8 -*-

""" The first string in the programe is the Doc string """
""" use by help function to describe the program """
import sys
def main():
    """ A 'Docstring' for the main function here"""
    print("you passed the argument " + sys.argv[1])

if __name__ == "__main__":
    main()
    