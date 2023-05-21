class Node:
    
    def __init__(self, i):
        self.data = [0] * (i+1)
        self.parent = None
        self.child = None

class Snail:
    
    currentNode = None
    x = 0
    count = 0
    number = 1
    
    def __init__(self):
        init = Node(0)
        self.root = init
        self.currentNode = self.root
    
    def __iter__(self):
        self.currentNode = self.root
        return self
    
    def __next__(self):
        self.currentNode = self.currentNode.child
        if self.currentNode:
            return self.currentNode.data
        else:
            raise StopIteration
    
    def append(self, i):
        newNode = Node(i)
        self.currentNode.child = newNode
        newNode.parent = self.currentNode
        self.currentNode = self.currentNode.child

    def init(self):
        self.currentNode = self.root
            
    def insertUp(self):
        self.x -= 1
        self.currentNode = self.currentNode.parent
        self.currentNode.data[self.x] =  self.number
        self.number += 1
        self.count += 1
    
    def insertDown(self):
        self.currentNode = self.currentNode.child
        self.currentNode.data[self.x] =  self.number
        self.number += 1
        self.count += 1
    
    def insertRight(self):
        self.x += 1
        self.currentNode.data[self.x] =  self.number
        self.number += 1
        self.count += 1
    
    
def solution(n):
    answer = []
    snail = Snail()
    for i in range(n):
        snail.append(i)
    snail.init()
    while n > 0:
        while snail.count < n:
            snail.insertDown()   
        else:
            snail.count = 0
            n -= 1
        while snail.count < n:
            snail.insertRight()
        else:
            snail.count = 0
            n -= 1
        while snail.count < n:
            snail.insertUp()
        else:
            snail.count = 0
            n -= 1
    for i in snail:
        answer.extend(i)        
    return answer