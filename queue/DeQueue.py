"""
    Double ended Queue: Insert and delete both of end (front/real)
"""

class DeQue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def insert_at_front(self, value):
        self.items.insert(0, value)

    def insert_at_end(self, value):
        self.items.append(value)

    def delete_at_front(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self.items.pop(0)
    
    def delete_at_end(self):
        if self.is_empty():
            print('Queue is empty')
            return
        return self.items.pop()