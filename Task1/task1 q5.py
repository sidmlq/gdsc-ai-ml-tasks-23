class FloatStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            return None 

    def empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        if not self.empty():
            print("Stack elements:")
            for element in self.stack:
                print(f"{element:.4f}")
        else:
            print("Stack is empty")

def main():
    stack = FloatStack()

    while True:
        print("\nOptions:")
        print("1 Push an element")
        print("2 Pop an element")
        print("3 Print all elements")
        print("4 Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            value = float(input("Enter a float value to push: "))
            stack.push(value)
        elif choice == '2':
            popped_value = stack.pop()
            if popped_value is not None:
                print(f"Popped element: {popped_value:.4f}")
            else:
                print("Underflow. Stack is empty.")
        elif choice == '3':
            stack.print_stack()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()