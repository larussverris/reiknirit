
# Skilaverkefni 4
class Node:
    def __init__ (self,v):
        self.value = v
        self.left = None
        self.right = None

    def insert(self,d):
        if self.value == d: # Eru þessi gögn þegar fyrir
            return False
        elif self.value > d: # Förum vinstra megin
            if self.left: # Er til leftChild
                return self.left.insert(d)
            else:
                self.left = Node(d) # Ef ekki til nýr hnútur búinn til
                return True

        else: # Förum hægra megin
            if self.right: # Er til rightChild
                return self.right.insert(d)
            else:
                self.right = Node(d) # Ef ekki til nýr hnútur búinn til
                return True



class Tree:
    def __init__(self):
        self.root = None

    def search(self, num, node = None):
        if node is None:
            node = self.root
            if node is None:
                return False

        if num == node.value:
            return True

        if node.left is not None:
            if self.search(num, node.left) is True:
                return True

        if node.right is not None:
            if self.search(num, node.right) is True:
                return True

        return False

    def insert(self,d):
        if self.root:
            return self.root.insert(d)
        else:
            self.root = Node(d)
            return True
t = Tree()
t.insert(6)
t.insert(2)
t.insert(3)
t.insert(7)

print(t.search(8)) # kallað á search fall
