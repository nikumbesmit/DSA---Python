# Leetcode - 225. Implement Stack using Queues

class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0

if __name__ == "__main__":
    stack = MyStack()
    
    print("=== Stack using Queues (LeetCode 225) ===")
    print("Commands:")
    print("  push <value> - Push a value onto the stack")
    print("  pop          - Remove and return the top element")
    print("  top          - Get the top element")
    print("  empty        - Check if the stack is empty")
    print("  exit         - Quit the program")
    print("-" * 40)

    while True:
        try:
            user_input = input("Enter command: ").strip()
            if not user_input:
                continue
            
            parts = user_input.split(maxsplit=1)
            cmd = parts[0].lower()
            
            if cmd == "exit":
                print("Exiting...")
                break
                
            elif cmd == "push":
                if len(parts) < 2:
                    print("Error: Please provide a value to push (e.g., push 5)")
                    continue
                try:
                    val = int(parts[1])
                    stack.push(val)
                    print(f"Pushed {val}")
                except ValueError:
                    print("Error: Push value must be an integer.")
                    
            elif cmd == "pop":
                print(f"Popped: {stack.pop()}")
                
            elif cmd == "top":
                print(f"Top: {stack.top()}")
                
            elif cmd == "empty":
                print(f"Is empty? {stack.empty()}")
                
            else:
                print(f"Unknown command: '{cmd}'. Use push, pop, top, empty, or exit.")
                
        except (IndexError, Exception) as e:
            print(f"Error: {e}")
