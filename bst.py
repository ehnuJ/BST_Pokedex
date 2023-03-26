'''
Name: Joon Hee Ooten
Date: 11/11/2022
Binary Search Tree
'''

from node import Node
from pokemon import Pokemon

class BST:
    def __init__(self):
        self._root = None
        
    def search(self, key):
        return self.recSearch(key, self._root)
    
    def recSearch(self, key, curNode):
        if curNode == None:
            raise IndexError("Not in tree")
        if curNode.entry == key:
            return curNode.entry
        if curNode.entry < key:
            return self.recSearch(key, curNode.right)
        if curNode.entry > key:
            return self.recSearch(key, curNode.left)
        else:
            raise RuntimeError("Not in tree")
        
    def add(self, entry):
        if self._root == None:
            self._root = Node(entry)
        elif self._root.entry < entry:
            if self._root.right == None:
                self._root.right = Node(entry)
            else:
                self.recAdd(entry, self._root.right)
        elif self._root.entry > entry:
            if self._root.left == None:
                self._root.left = Node(entry)
            else:
                self.recAdd(entry, self._root.left)
        else:
            raise RuntimeError("No Duplicates")
    
    def recAdd(self, entry, curNode):
        if curNode.entry < entry:
            if curNode.right == None:
                curNode.right = Node(entry)
            else:
                self.recAdd(entry, curNode.right)
        elif curNode.entry > entry:
            if curNode.left == None:
                curNode.left = Node(entry)
            else:
                self.recAdd(entry, curNode.left)
        else:
            raise RuntimeError("No Duplicates")
    
    def remove(self, key):
        if self._root == None:
            raise RuntimeError("Empty Tree")
        else:
            self.recRemove(key, self._root)
    
    def recRemove(self, key, curNode):
        if curNode.entry > key:
            curNode.left = self.recRemove(key, curNode.left)
        elif curNode.entry < key:
            curNode.right = self.recRemove(key, curNode.right)
        else:
            if curNode.left == None and curNode.right == None:
                curNode == None
                return None
            elif curNode.left == None:
                temp = curNode.right
                curNode = None
                return temp
            elif curNode.right == None:
                temp = curNode.left
                curNode = None
                return temp
            else:
                temp = self.gst(curNode.left)
                curNode.entry = temp.entry
                self.recRemove(temp.entry.ID, curNode.left)
        return curNode
    
    def preOrder(self, visit):
        if self._root != None:
            self.recPreOrder(visit, self._root)
    
    def recPreOrder(self, visit, curNode):
        visit(curNode.entry)
        if curNode.left != None:
            self.recPreOrder(visit, curNode.left)
        if curNode.right != None:
            self.recPreOrder(visit, curNode.right)
            
    def inOrder(self, visit):
        if self._root != None:
            self.recInOrder(visit, self._root)
    
    def recInOrder(self, visit, curNode):
        if curNode.left != None:
            self.recInOrder(visit, curNode.left)
        visit(curNode.entry)
        if curNode.right != None:
            self.recInOrder(visit, curNode.right)
        
    def postOrder(self, visit):
        if self._root != None:
            self.recPostOrder(visit, self._root)
    
    def recPostOrder(self, visit, curNode):
        if curNode.left != None:
            self.recPostOrder(visit, curNode.left)
        if curNode.right != None:
            self.recPostOrder(visit, curNode.right)
        visit(curNode.entry)
        
    def gst(self, curNode):
        if curNode.right == None:
            return curNode
        else:
            return self.gst(curNode.right)