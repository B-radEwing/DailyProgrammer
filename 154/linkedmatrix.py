#Linked Matrix
from node import Node

class LinkedMatrix(object):

    def __init__(self, x, y, defaultValue):
        self.head = Node(defaultValue)
        self.X = x
        self.Y = y
        self.default = defaultValue

        countX = 0
        countY = 0
        count = 0
        WestNode = self.head
        currentNode = self.head
        currentTopNode = self.head
        
        while countY < y:
            while countX < x:
                currentNode.east = Node(defaultValue)
                tempNode = currentNode
                currentNode = currentNode.east
                currentNode.west = tempNode
                if WestNode.north != None:
                    currentNode.north = currentTopNode
                    currentTopNode.south = currentNode
                    currentTopNode = currentTopNode.east
                countX += 1

            WestNode.south = Node(defaultValue)
            currentNode = WestNode.south
            currentNode.north = WestNode
            currentTopNode = WestNode.east
            WestNode = WestNode.south
            countX = 0
            countY += 1


        countY = 0
        countX = 0
        currentNode = self.head
        while countY < (y- 1):
            currentNode = currentNode.south
            countY += 1

        topNode = self.head

        while countX < x:
            currentNode.south = topNode
            topNode.north = currentNode

            topNode = topNode.east
            currentNode = currentNode.east
            countX += 1

        countY = 0
        countX = 0
        currentNode = self.head
        while countX < (x - 1):
            currentNode = currentNode.east
            countX += 1
        leftNode = self.head

        while countY < y:
            currentNode.east = leftNode
            leftNode.west = currentNode
            leftNode = leftNode.south
            currentNode = currentNode.south
            countY += 1
            

                
    def __str__(self):
        MatrixStr = ""
        WestNode = self.head
        CurrentNode = self.head
        countX = 0
        countY = 0

        while countY < (self.Y):
            while countX < (self.X):
                MatrixStr += str(CurrentNode.getValue()) + " "
                CurrentNode = CurrentNode.east
                countX += 1
            countX = 0
            MatrixStr += "\n"
            WestNode = WestNode.south
            CurrentNode = WestNode
            countY += 1

        


        return MatrixStr

    def __getitem__(self,index):
        x = index[0]
        y = index[1]
        count = 0
        currentNode = self.head

        while x > count:
            currentNode = currentNode.east
            count += 1
        count = 0

        while y > count:
            currentNode = currentNode.south
            count += 1

        return currentNode.value

    

    def __setitem__(self, index, a):
        x = index[0]
        y = index[1]
        count = 0
        currentNode = self.head

        while x > count:
            currentNode = currentNode.east
            count += 1
        count = 0

        while y > count:
            currentNode = currentNode.south
            count += 1

        currentNode.value = a

    
