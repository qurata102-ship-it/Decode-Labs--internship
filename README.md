📝 To-Do List Application

A simple **Console-Based To-Do List Application** built with Python as part of my Python internship at **DECODE Labs**.

The project allows users to create, view, complete, and delete tasks while storing task data permanently in a JSON file.

 🚀 Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 Save tasks using JSON persistence
* 🔄 Load previously saved tasks when the application starts
* 🖥️ Simple console-based interface

 🛠️ Technologies Used

* **Python 3**
* **JSON** — for persistent data storage
* **OS module** — for checking whether the storage file exists

 📂 Project Structure

```text
pro 1 to do list/
│
├── main.py
├── menu.py
├── storage.py
├── task_manager.py
├── tasks.json
└── README.md
```

 🧠 Concepts Practiced

This project helped me practice several Python fundamentals:

* Variables
* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* File handling
* JSON serialization and deserialization
* Modules and imports
* Basic CRUD operations
* Persistent data storage

 🔄 How It Works

When the application starts, it loads previously saved tasks from `tasks.json`.

Each task is represented as a dictionary:

```python
{
    "id": 1,
    "title": "Study Python",
    "completed": False
}
```

Multiple task dictionaries are stored inside a list:

```python
tasks = [
    {
        "id": 1,
        "title": "Study Python",
        "completed": False
    }
]
```

When a new task is added, it is added to the list using:

```python
tasks.append(task)
```

The list is then saved to `tasks.json`.

 ▶️ How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code and run:

```bash
python main.py
```

The application will display a menu:

```text
TO-DO LIST
1. Add Task
2. View Tasks
3. Mark Task Complete
4. Delete Task
5. Exit
```

Choose an option and follow the instructions displayed in the terminal.

 💾 Data Persistence

The application uses a JSON file to store tasks.

This means tasks are not lost when the program is closed.

For example:

```json
[
    {
        "id": 1,
        "title": "Learn Python",
        "completed": true
    }
]
```

When the program starts again, the saved tasks are loaded automatically.

 🎯 Learning Objective

The main goal of this project was to understand how Python can be used to build a simple real-world application while practicing data structures, functions, file handling, and persistent storage.

👩‍💻 Internship Project

**Python Internship — DECODE Labs**

This project is part of my learning journey as a Python Intern, where I am developing practical projects to strengthen my programming and problem-solving skills.

---
