class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Stack:

    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(node.value) for node in self.LinkedList]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    
    def pop(self):
        if self.isEmpty():
            print ("The stack is empty.")
        else:
            print(f'Popped {self.LinkedList.head.value}')
            self.LinkedList.head = self.LinkedList.head.next

    def peek(self):
        if self.isEmpty():
            print ("The stack is empty.")
        else:
            print(f'Peek is {self.LinkedList.head.value}')

    def delete(self):
        self.LinkedList.head = None

def main():
    stack = Stack()
    print(stack.isEmpty())
    stack.push(1)
    print(stack)
    stack.pop()
    stack.pop()
    stack.push(1)   
    stack.push(2)
    stack.push(3)
    stack.push(4)   
    stack.push(5)
    stack.push(6)
    stack.isEmpty
    print(stack)
    stack.peek()
    stack.pop()
    print(stack)
    stack.peek()
    stack.delete()
    print(stack.isEmpty())

main()