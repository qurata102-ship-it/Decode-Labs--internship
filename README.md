📝 To-Do List Application

A simple **Console-Based To-Do List Application** built with Python as part of my Python internship at **DECODE Labs**.

The project allows users to add tasks to a list and display their complete To-Do List.

🚀 Features

- ➕ Add new tasks
- 📋 Store multiple tasks in a list
- 👀 Display the complete To-Do List
- 🖥️ Simple console-based interface

🛠️ Technology Used

- **Python 3**

🧠 Concepts Practiced

This project helped me practice fundamental Python concepts:

- Lists
- `append()`
- Variables
- `input()`
- `while` loops
- `for` loops
- `if` statements
- User input
- Basic data processing

 🔄 How It Works

The program first creates an empty list:

```python
todo_list = []
````

The user enters a task, which is stored in a variable:

```python
new_task = input("Add new task: ")
```

The task is then added to the list using `append()`:

```python
todo_list.append(new_task)
```

The user can continue adding tasks.

After finishing, the program asks whether the user wants to view the To-Do List. If the user chooses `yes`, a `for` loop displays every task:

```python
for task in todo_list:
    print(task)
```

 ▶️ How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code and run:

```bash
python todo.py
```

The program will allow you to enter tasks and choose whether you want to view your complete To-Do List.

 📌 Example

```text
Add new task: Study Python
Add another? (yes or no): yes

Add new task: Practice Git
Add another? (yes or no): no

Do you want to see your To-Do List? (yes or no): yes

Study Python
Practice Git
```

 🎯 Learning Objective

The main objective of this project was to understand how Python **lists**, `append()`, loops, and user input can be used to build a simple task-management program.

👩‍💻 Internship Project

**Python Internship — DECODE Labs**

This project is part of my learning journey as a Python Intern, where I am developing practical projects to strengthen my programming and problem-solving skills.