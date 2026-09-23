#  Reverse the given stack using Recursion

def insert_at_bottom(st: list[int], element: int) -> None:
    if not st:
        st.append(element)
        return

    temp: int = st.pop()
    insert_at_bottom(st,element)
    st.append(temp)


def reverse_stack(st: list[int]) -> None:
    if not st:
        return

    temp: int = st.pop()
    reverse_stack(st)
    insert_at_bottom(st, temp)


if __name__ == "__main__":
    user_input: str = input("Enter stack elements separated by spaces: ")
    stack: list[int] = [int(x) for x in user_input.split()]

    reverse_stack(stack)

    print("Reversed Stack:", stack)
    if stack:
        print("Top Element:", stack[-1])
