"""
    Queue: (FIFO) First in first out
"""
class QueueOperation:
    
    def __init__(self):
        self.queue = []

    def is_empty_queue(self):
        return len(self.queue) == 0 

    # Insert element into queue
    def insert(self, value):
        self.queue.append(value)
       
    def delete(self):
        if self.is_empty_queue():
            raise('Queue is empty')
        return self.queue.pop(0)

q = QueueOperation()

q.insert(10)
q.insert(20)
q.insert(30)
print(q.queue)
print(q.delete())
print(q.delete())
print(q.delete())
print(q.queue)
print(q.delete())