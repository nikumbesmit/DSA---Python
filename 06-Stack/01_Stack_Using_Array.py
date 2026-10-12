# Implementing Stack using Array 

class MyStack :

    def __init__(self):
        self.arr = []

    def Push(self,data) :
        self.arr.append(data)

    def Pop(self) :
        if len(self.arr) == 0 :
            return -1
        else :
            return self.arr.pop()
        

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
                    stack.Push(val)
                elif query_type == 2:
                    print(stack.Pop(), end=" ")
                    
            print()
