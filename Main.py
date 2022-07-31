import os
class Stack:
    def __init__(self, size):
        self.items = []
        self.size = size

    def is_empty(self):
        # Write code here
        return len(self.items)==0
        

    def is_full(self):
        # Write code here
        return len(self.items)==100

    def push(self, data):
        if not self.is_full():
            # Write code here
            self.items.append(data)
            self.size=+1
           
            

    def pop(self):
        if not self.is_empty():
            # Write code here
            self.items.pop()
            self.size-=1
            

    def status(self):
        # Write code here
        for item in self.items:
            print(item)

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
   
    
 
    

