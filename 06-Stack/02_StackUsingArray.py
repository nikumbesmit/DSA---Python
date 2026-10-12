# Implementation of Stack using LinkedList

class StackNode :

    def __init__(self,data):
        self.data = data
        self.next = None

class MyStack :

    def __init__(self):
        self.top = None

    def push(self,data) :
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self) :
        if self.top is None :
            return -1

        popped_data = self.top.data
        self.top = self.top.next

        return popped_data
    

if __name__ == "__main__":
    stack = MyStack()
    
    user_input = input("Enter queries: ").strip().split()
    
    if user_input:
        iterator = iter(user_input)
        t = int(next(iterator)) 
        
        for _ in range(t):
            q = int(next(iterator)) 

            for _ in range(q):
                query_type = int(next(iterator))
                if query_type == 1:
                    val = int(next(iterator))
                    stack.push(val)
                elif query_type == 2:
                    print(stack.pop(), end=" ")
                    
            print()
