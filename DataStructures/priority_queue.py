import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def isEmpty(self):
        return not self.elements
    
    def put(self, item, priority):
        heapq.heappush(self.elements,(priority,item))
    
    def get(self):
        if not self.isEmpty(): 
           return heapq.heappop(self.elements)[1]
        return None

    def __str__(self):
        return str(self.elements)
    
if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq.isEmpty())
    pq.put(100,1)
    pq.put(200,1)
    pq.put(200,4)
    pq.put(300,2)
    print(pq)
    print(pq.get())
    print(pq.get())
    print(pq)
    print(pq.get())
    print(pq.get())