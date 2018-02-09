class MyQueue(object):
    def __init__(self):
        self.data = []
        self.n = 0
        
    def peek(self):
        if self.n > 0:
            return self.data[self.n - 1]
        
        return None
    
    def pop(self):
        self.n = self.n - 1
        
        return self.data.pop()
        
    def put(self, value):
        self.data.insert(0, value)
        self.n = self.n + 1

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

