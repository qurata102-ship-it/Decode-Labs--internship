#adding list
todo_list = []
answer = "yes"
#adding new task
while answer == "yes":
 new_task = input("Add new task: ")
 #appending list
 todo_list.append(new_task)
 #asking for user's choice to add a task or not
 answer = input ("Add another?(yes or no)") 

to_view_list = input("Do you want to see your To-Do List? (yes or no): ")
if to_view_list == "yes":
    for task in todo_list:
        print(task)
for task in todo_list:
    print(task)