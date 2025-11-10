class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return not self.items
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
           return self.items.pop()
        return None
    
    def peek(self):
        if not self.isEmpty():
           return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)
    
if __name__ == "__main__":
    s = Stack()
    print(s) # []
    s.push(10) 
    s.push(344) 
    print(s) # [10,344]
    print(s.isEmpty()) # false
    print(s.pop()) # 344
    print(s) # [10]
    print(s.peek()) # 10
    print(s.size()) # 1
    print(s.pop())
    print(s.peek())
    print(s.isEmpty())
    print(s.size())
    print(s.pop())
