todo_list = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list, start=1):
        print(f"{i}. {task}")

    print("\nOptions:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Quit")

    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == "2":
        index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    elif choice == "3":
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")