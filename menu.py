from storage import load_tasks
from tasks_manager import (
    add_task,
    view_tasks,
    complete_task,
    delete_task
)
def menu():
    tasks = load_tasks()

    while True:
        print("\nTO-DO LIST ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("\nThank you for using To-Do List!")
            break

        else:
            print("\nInvalid choice! Please try again.")