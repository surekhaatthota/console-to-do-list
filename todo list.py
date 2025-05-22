todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print("Task added successfully!")

    elif choice == "2":
        if not todo_list:
            print("Your to-do list is empty.")
        else:
            print("\n--- Your Tasks ---")
            for idx, item in enumerate(todo_list, start=1):
                status = "Done" if item["done"] else "Not Done"
                print(f"{idx}. {item['task']} [{status}]")
    elif choice == "3":
        num = int(input("Enter the task number to mark as done: "))
        if 0 < num <= len(todo_list):
            todo_list[num - 1]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")

    elif choice == "4":
        num = int(input("Enter the task number to delete: "))
        if 0 < num <= len(todo_list):
            deleted = todo_list.pop(num - 1)
            print(f"Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")

    elif choice == "5":
        print("Exiting the To-Do List App. Goodbye!")
        break

    else:
        print("Please enter a valid option (1-5).")
