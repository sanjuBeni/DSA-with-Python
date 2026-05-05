class Node:
    def __init__(self, info, next = None):
        self.data = info
        self.next = next

class SingleLinkedList:
    def __init__(self, head = None):
        self.head = head

    # Insert Node at Beginner
    def insert_node_beginner(self, value):
        new_node = Node(value)
        head = self.head
        if(head is None):
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        return
    
    # Insert Node at End
    def insert_node_end(self, value):
        new_node = Node(value)
        head = self.head
        if(head is None):
            self.head = new_node
            return
        
        while True:
            if(head.next is None):
                break
            head = head.next

        head.next = new_node
        return
    
    # Insert Node at a specification position
    def insert_node_at_position(self, value, pos):
        new_node = Node(value)
        head = self.head
        if(head is None):
            self.head = new_node
            return
        
        while True:
            if head.data == pos:
                break
            if head.next is None:
                break
            head = head.next

        if head.data != pos:
            print(f"Data {pos} is not found")
            return
        
        new_node.next = head.next
        head.next = new_node
        

        return
    
    # Get all node data
    def get_node(self):
        head = self.head
        if(head is None):
            print("Linked list is empty.")
            return
        
        while True:
            print(head.data, end=", ")
            if(head.next is None):
                break
            head = head.next

l = SingleLinkedList()
l.insert_node_beginner(40)
l.insert_node_beginner(30)
l.insert_node_beginner(20)
l.insert_node_beginner(10)
l.insert_node_end(50)
l.insert_node_end(70)
l.insert_node_at_position(60, 50)
l.get_node()