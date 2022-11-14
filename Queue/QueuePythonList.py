class Queue:

    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list
        values = [str(value) for value in values]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            False
    
    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            print ("The queue is empty.")
        else:
            print(f'Dequeued {self.list.pop(0)}')
    
    def peek(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.list[0]
        
    def delete(self):
        self.list = []

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
    print(queue)
    queue.dequeue()
    print(queue.peek())
    queue.dequeue()
    queue.isEmpty
    print(queue)
    queue.dequeue()
    print(queue)
    queue.delete()
    print(queue.isEmpty())

main()