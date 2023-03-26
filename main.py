'''
Name: Joon Hee Ooten
Date: 11/11/2022
Contains main function
'''

from bst import BST
from executive import Executive

def main():
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive(file_name)
    my_exec.run()

main()