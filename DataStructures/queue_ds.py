from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.isEmpty():
           return self.items.popleft()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[0]
        return None

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return not self.items
    
    def __str__(self):
        return str(self.items)

if __name__ == '__main__':
    q = Queue()
    q.enqueue(100)
    print(q)
    print(q.isEmpty())
    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(200)
    q.enqueue(300)
    q.enqueue(200)
    q.enqueue(300)
    print(q)
    print(q.size())
    print(q.peek())
    print(q.dequeue())