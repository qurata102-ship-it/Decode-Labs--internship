todo_list = []
answer = "yes"
while answer == "yes":
 new_task = input("Add new task: ")
 todo_list.append(new_task)
 answer = input ("Add another?(yes or no)") 


for task in todo_list:
    print(task)