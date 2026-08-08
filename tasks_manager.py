from storage import save_tasks
def add_task(tasks):
    title = input("Enter task title: ")
    if tasks:
        next_id = tasks[-1]["id"] + 1
    else:
        next_id = 1
    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\nTask List")
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        print(f'ID: {task["id"]} | {status} | {task["title"]}')
    print()
def complete_task(tasks):
    task_id = int(input("Enter Task ID: "))
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed!\n")
            return
    print(" Task not found.\n")
def delete_task(tasks):
    task_id = int(input("Enter Task ID: "))
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(" Task deleted successfully!\n")
            return
    print(" Task not found.\n")