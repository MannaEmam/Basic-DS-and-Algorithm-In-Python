class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        return "The DLL has been created."

    def insertDLL(self, value, loc):
        if self.head is None:
            return "The head reference is None."
        else:
            newNode = Node(value)
            if loc == 0:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif loc == 1:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                node = self.head
                index = 0
                while index < loc - 1:
                    node = node.next
                    index += 1
                temp = node.next
                newNode.prev = node
                temp.prev = newNode
                newNode.next = node.next
                node.next = newNode
    
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse.")
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next
    
    def reverseTraverse(self):
        if self.head is None:
            print("There is not any element to traverse.")
        else:
            node = self.tail
            while node:
                print(node.value)
                node = node.prev
    
    def searchDLL(self, value):
        if self.head is None:
            return "There is not any element in the list."
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
            return "The node does not exist in this list."

    def deleteNode(self, value):
        if self.head is None:
            return "There is not any element in the list."
        
        elif value == self.head.value:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None

        elif value == self.tail.value:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            node = self.head
            while node:
                if node.value == value:
                    break
                node = node.next
            temp = node.prev
            node.next.prev = temp
            temp.next = node.next

    def deleteDLL(self):
        if self.head is None:
            return "There is not any element in the list."
        
        else:
            node = self.head
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None


            
    
dll = DoublyLL()
print(dll.createDLL(1))
dll.insertDLL(0, 0)
dll.deleteNode(0)
dll.reverseTraverse()
print([node.value for node in dll])
dll.insertDLL(2, 1)
dll.insertDLL(4, 1)
dll.insertDLL(5, 1)
dll.reverseTraverse()
print([node.value for node in dll])
dll.insertDLL(3, 3)
print([node.value for node in dll])
dll.reverseTraverse()
dll.traverseDLL()
print(dll.searchDLL(4))
print(dll.searchDLL(6))
# dll.deleteNode(0)
# dll.reverseTraverse()
# print([node.value for node in dll])
dll.deleteNode(5)
dll.reverseTraverse()
print([node.value for node in dll])
dll.deleteNode(2)
dll.reverseTraverse()
print([node.value for node in dll])
dll.deleteDLL()
print([node.value for node in dll])