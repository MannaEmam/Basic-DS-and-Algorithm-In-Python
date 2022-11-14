class Stack:
    
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list[::-1]
        values = [str(x) for x in values]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            False

    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            print ("The stack is empty.")
        else:
            print(f'Popped {self.list.pop()}')
    
    def peek(self):
        if self.isEmpty():
            print ("The stack is empty.")
        else:
            print (self.list[len(self.list) - 1])
        
    def delete(self):
        self.list = []

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
    stack.pop()
    print(stack)
    stack.peek()
    stack.delete()
    print(stack.isEmpty())

main()
    