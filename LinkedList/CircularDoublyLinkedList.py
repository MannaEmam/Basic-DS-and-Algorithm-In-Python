class Node:
    
    def __init__(self, value = None):
        self.prev = None
        self.value = value
        self.next = None
    
class CircularDoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCDLL(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
        return "The CDLL is created successfully"

    def insertCDLL(self, value, loc):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if loc == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif loc == 1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
                self.head.prev = newNode
            else:
                index = 0
                node = self.head
                while index < loc - 1:
                    index += 1
                    node = node.next
                temp = node.next
                newNode.prev = node
                newNode.next = temp
                temp.prev = newNode
                node.next = newNode
    
    def traverseCDLL(self):
        if self.head is None:
            return "There is not any element for traversal."
        temp = self.head
        while temp:
            print(temp.value,end=" ")
            temp = temp.next
            if temp == self.tail.next:
                break
    
    def reverseTraverseCDLL(self):
        if self.head is None:
            print("There is not any element to traverse.")
        else:
            node = self.tail
            while node:
                print(node.value,end=" ")
                node = node.prev
                if node == self.head.prev:
                    break
    
    def searchCDLL(self, value):
        if self.head is None:
            return "There is not any element in the list."
        else:
            node = self.head
            while node:
                if node.value == value:
                    return node.value
                node = node.next
                if node == self.tail.next:
                    return "The node does not exist in this CDLL."

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

    def deleteCDLL(self):
        if self.head is None:
            return "There is not any element in the list."
        else:
            node = self.head
            self.tail.next = None
            while node:
                node.prev = None
                node = node.next
            self.head = None
            self.tail = None


def main():
    cdll = CircularDoublyLinkedList()
    print(cdll.createCDLL(1))
    cdll.insertCDLL(0, 0)
    # dll.deleteNode(0)
    # dll.reverseTraverse()
    print([node.value for node in cdll])
    cdll.insertCDLL(2, 1)
    cdll.insertCDLL(4, 1)
    cdll.insertCDLL(5, 1)
    # cdll.reverseTraverse()
    # print([node.value for node in dll])
    cdll.insertCDLL(3, 3)
    print([node.value for node in cdll])
    # dll.reverseTraverse()
    cdll.traverseCDLL()
    print(cdll.searchCDLL(4))
    # print(dll.searchDLL(6))
    cdll.deleteNode(0)
    cdll.reverseTraverseCDLL()
    print(f'\n{[node.value for node in cdll]}')
    # dll.deleteNode(5)
    # dll.reverseTraverse()
    # print([node.value for node in dll])
    # dll.deleteNode(2)
    # dll.reverseTraverse()
    # print([node.value for node in dll])
    cdll.deleteCDLL()
    print([node.value for node in cdll])

main()
                
