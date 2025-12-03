import heapq
class PriorityQueueWithoutPriority:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        heapq.heappush(self.items,item)
    
    def pop(self):
        return heapq.heappop(self.items)

    def isEmpty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def get(self,idx):
        return self.items[idx]
