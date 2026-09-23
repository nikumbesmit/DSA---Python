# Sort the stack in such a way that the top of the stack has the greatest element

def sorted_insert(s: list[int], element: int) -> None:
    if not s or s[-1] <= element:
        s.append(element)
        return

    temp: int = s.pop()
    sorted_insert(s, element)
    s.append(temp)


def sort_stack(s: list[int]) -> None:
    if not s:
        return

    temp: int = s.pop()
    sort_stack(s)
    sorted_insert(s, temp)


if __name__ == "__main__":
    user_input: str = input("Enter stack elements separated by spaces: ")
    stack: list[int] = [int(x) for x in user_input.split()]

    sort_stack(stack)

    print("Sorted Stack:", stack)
    if stack:
        print("Top Element:", stack[-1])
