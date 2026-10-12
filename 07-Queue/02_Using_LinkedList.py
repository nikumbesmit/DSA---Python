# Implementing Queue using LinkedList

class QueueNode :

    def __init__(self,data):
        self.data = data
        self.next = None

class MyQueue :

    def __init__(self):
        self.front = None
        self.rear = None 

    def push(self, item) :
        new_node = QueueNode(item)
        if self.rear is None :
            self.front = self.rear = new_node
        else :
            self.rear.next = new_node
            self.rear = new_node

    def pop(self) :
        if self.front is None :
            return -1
        popped_item = self.front.data
        self.front = self.front.next

        if self.front is None :
            self.rear = None

        return popped_item

if __name__ == "__main__":
    queue = MyQueue()
    
    user_input = input("Enter operations (e.g., 1 10 for push, 2 for pop): ").strip().split()
    
    if user_input:
        iterator = iter(user_input)
        
        try:
            while True:
                query_type = int(next(iterator))
                
                if query_type == 1:
                    val = int(next(iterator))
                    queue.push(val)
                    
                elif query_type == 2:
                    print(queue.pop(), end=" ")
                    
        except StopIteration:
            pass
            
        print()

