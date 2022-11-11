from nntplib import NNTPDataError
from platform import node

from django.urls import clear_script_prefix
from requests import head


class Node:
    
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created."
    
    def insertCSLL(self, nodeValue, location):
        if self.head is None:
            return "The head reference is None."
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                temp = node.next
                node.next = newNode
                newNode.next = temp
            return "The node has been successfully inserted"
    def traverseCSLL(self):
        if self.head is None:
            return "There is not any element for traversal."
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
            if temp == self.tail.next:
                break
    def searchCSLL(self, value):
        if self.head is None:
            "There is not any node in this CSLL."
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == value:
                    return tempNode.value
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL."
    def deleteNode(self, location):
        if self.head is None:
            "There is not any node in this CSLL."
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head 
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    self.tail = node
            else:
                index = 0
                node = self.head
                while index < location - 1:
                    node = node.next
                    index += 1
                temp = node.next
                node.next = temp.next
    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None
circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(1))
circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(2,2)
print([node.value for node in circularSLL])
# circularSLL.traverseCSLL()
# print(circularSLL.searchCSLL(5))
# circularSLL.deleteNode(4)
circularSLL.deleteEntireCSLL()
print([node.value for node in circularSLL])