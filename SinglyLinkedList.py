from math import sin


class Node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
class SLinkedList():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def findLocation(self):
        i = 1
        while self.head is not None:
            self.head = self.head.next
            i += 1
        return i

    def insertSLL(self, value, loc):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            if loc == 0:
                newNode.next = self.head
                self.head = newNode 
            elif loc == 1:
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < loc - 1 :
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def traverseSLL(self):
        if self.head is None:
            print("The list doesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    def searchSLL(self, val):
        if self.head is None:
            return "The list doesn't exist"
        else:
            node = self.head
            while node is not None:
                if val == node.value:
                    return node.value
                node = node.next
            return "The value does not exist in this list"
    def deleteNode(self, loc):
        if self.head is None:
            print("The list doesn't exist")
        else:
            if loc == 0:
                if self.head.next is None:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loc == 1:
                if self.head.next is None:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node.next is not None:
                        tempNode = node
                        node = node.next
                    tempNode.next = None
                    self.tail = tempNode
            else:
                    node = self.head
                    index = 0
                    while index < loc - 1:
                        print(f'{index} {node.value}')
                        node = node.next
                        index += 1
                    nextNode = node.next
                    node.next = nextNode.next
    def deleteEntireSLL(self):
        if self.head is None:
           print("The list doesn't exist")
        else:
            self.head = None
            self.tail = None
                    

singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5, 3)
singlyLinkedList.insertSLL(0, 0)
print([node.value for node in singlyLinkedList]) 
# singlyLinkedList.traverseSLL()
# singlyLinkedList.deleteNode(3)
# singlyLinkedList.traverseSLL()
# print([node.value for node in singlyLinkedList]) 
# singlyLinkedList.deleteEntireSLL()
# print([node.value for node in singlyLinkedList]) 
print(singlyLinkedList.findLocation())
