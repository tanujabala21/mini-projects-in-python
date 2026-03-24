tasks_file = "file.txt"

def add_task():
    task = input("Enter task: ")
    with open(tasks_file, "a") as file:
        file.write(task + "\n")
    print("Task added ")

def view_tasks():
    try:
        with open(tasks_file, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found")
            return

        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t.strip()}")

    except FileNotFoundError:
        print("No tasks yet")


def delete_task():
    try:
        with open(tasks_file, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete ")
            return

        view_tasks()
        num = int(input("Enter task number to delete: "))

        if num < 1 or num > len(tasks):
            print("Invalid number ")
            return

        tasks.pop(num - 1)

        with open(tasks_file, "w") as file:
            file.writelines(tasks)

        print("Task deleted")

    except FileNotFoundError:
        print("No file found ")


def mark_done():
    try:
        with open(tasks_file, "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks available ")
            return

        view_tasks()
        num = int(input("Enter task number to mark as done: "))

        if num < 1 or num > len(tasks):
            print("Invalid number")
            return

        tasks[num - 1] = tasks[num - 1].strip() + "\n"

        with open(tasks_file, "w") as file:
            file.writelines(tasks)

        print("Task marked as done ")

    except FileNotFoundError:
        print("No file found ")

while True:
    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_done()
    elif choice == "5":
        print("Goodbye ")
        break
    else:
        print("Invalid choice ")