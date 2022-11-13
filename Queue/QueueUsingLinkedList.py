class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:

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

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.LinkedList.head = node
            self.LinkedList.tail = node
        else:
            self.LinkedList.tail.next = node
            self.LinkedList.tail = node
    
    def dequeue(self):
        if self.isEmpty():
            print ("The queue is empty.")
        else:
            print(f'Dequeued {self.LinkedList.head.value}')
            self.LinkedList.head = self.LinkedList.head.next
    
    def peek(self):
        if self.isEmpty():
            print ("The queue is empty.")
        else:
            print(f'Peek is {self.LinkedList.head.value}')

    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

def main():
    queue = Queue()
    print(queue.isEmpty())
    queue.enqueue(1)
    print(queue)
    queue.dequeue()
    queue.dequeue()
    queue.enqueue(1)   
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)   
    queue.enqueue(5)
    queue.enqueue(6)
    queue.dequeue()
    queue.peek()
    queue.dequeue()
    queue.isEmpty
    print(queue)
    queue.dequeue()
    print(queue)
    queue.delete()
    print(queue.isEmpty())

main()