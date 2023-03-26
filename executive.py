'''
Name: Joon Hee Ooten
Date: 11/11/2022
Executive class with menu options
'''

from pokemon import Pokemon
from bst import BST

class Executive:
    def __init__(self, input):
        self.choice = ""
        self.file_name = input
        self.pokedex = BST()
        self.copyPokedex = BST()
        
    def printMenu(self):
        print("1) Search")
        print("2) Add")
        print("3) Print")
        print("4) Copy")
        print("5) Remove")
        print("6) Quit")
    
    def readData(self):
        from os.path import dirname, join
        current = dirname(__file__)
        file_path = join(current, self.file_name)
        input_file = open(file_path)
        list = []        
        for line in input_file:
            line = line.translate({ord(c): None for c in '\n'})
            list = line.split(" ")
            tempAname = list[0]
            tempID = int(list[1])
            tempJname = list[2]
            new = Pokemon(tempAname, tempID, tempJname)
            self.pokedex.add(new)
    
    def printPokemon(self, pokemon):
        print(pokemon)
        
    def copy(self):
        self.copyPokedex.preOrder(self.copyPokedex.add)
        
    def run(self):
        self.readData()
        x = 0
        while self.choice != 6:
            self.printMenu()
            self.choice = int(input("Menu choice: "))
            if self.choice == 1:
                if x != 1:
                    key = int(input("Pokedex number: "))
                    print(self.pokedex.search(key))
                else:
                    tree = input("Which Pokedex? Select O for original and C for copy: ")
                    if tree == "O" or "o":
                        key = int(input("Pokedex number: "))
                        print(self.pokedex.search(key))
                    elif tree == "C" or "c":
                        key = int(input("Pokedex number: "))
                        print(self.copyPokedex.search(key))
            if self.choice == 2:
                if x != 1:
                    usa = input("American Name: ")
                    jp = input("Japanese Name: ")
                    num = int(input("Pokedex #: "))
                    self.pokedex.add(Pokemon(usa, num, jp))
                else:
                    tree = input("Which Pokedex? Select O for original and C for copy: ")
                    usa = input("American Name: ")
                    jp = input("Japanese Name: ")
                    num = int(input("Pokedex #: "))
                    if tree == "O" or "o":
                        self.pokedex.add(Pokemon(usa, num, jp))
                    elif tree == "C" or "c":
                        self.copyPokedex.add(Pokemon(usa, num, jp))
            if self.choice == 3:
                print("1) Pre Order")
                print("2) In Order")
                print("3) Post Order")
                order = int(input("What order? "))
                if x != 1:
                    if order == 1:
                        self.pokedex.preOrder(self.printPokemon)
                    elif order == 2:
                        self.pokedex.inOrder(self.printPokemon)
                    elif order == 3:
                        self.pokedex.postOrder(self.printPokemon)
                else:
                    tree = input("Which Pokedex? Select O for original and C for copy: ")
                    if tree == "O" or "o":
                        if order == 1:
                            self.pokedex.preOrder(self.printPokemon)
                        elif order == 2:
                            self.pokedex.inOrder(self.printPokemon)
                        elif order == 3:
                            self.pokedex.postOrder(self.printPokemon)
                    elif tree == "C" or "c":
                        if order == 1:
                            self.copyPokedex.preOrder(self.printPokemon)
                        if order == 2:
                            self.copyPokedex.inOrder(self.printPokemon)
                        if order == 3:
                            self.copyPokedex.postOrder(self.printPokemon)
            if self.choice == 4:
                if x != 1:
                    self.copy()
                    x = 1
                else:
                    print("Copy already exists")
            
            if self.choice == 5:
                remove = int(input("What Pokemon would you like to remove? ID #: "))
                if x != 1:
                    self.pokedex.remove(remove)
                else:
                    tree = input("Which Pokedex? Select O for original and C for copy: ")
                    if tree == "O" or "o":
                        self.pokedex.remove(remove)
                    elif tree == "C" or "c":
                        self.copyPokedex.remove(remove)