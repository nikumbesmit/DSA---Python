# Implementing Queue using an Array

class MyQueue :

    def __init__(self):
        self.queue = []

    def push(self, data) :
        self.queue.append(data)

    def pop(self) :
        if len(self.queue) == 0 :
            return -1
        else :
           return self.queue.pop(0)
        

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
