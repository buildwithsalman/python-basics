tasks = []
task_number = 1

def show_tasks():
    if not tasks:
        print("There is nothing to show you.")
    else :
        for i, t in enumerate(tasks,start=1):
            print(f"{i}) {t}")

while True :
    print("----TO DO LIST----")
    print("1) Add new task")
    print("2) View all task")
    print("3) Mark a task as done")
    print("4) Delete a task as done")
    print("5) Exit")
    print("-----------------")

    try:
        option = int(input("Enter the option number: "))
    
    except ValueError:
        print("print a valid option")
        continue


    if (option == 1):
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif (option ==2 ):
        if not tasks :
            print ("OOPS.. There is nothing to show you.")
        else :
            show_tasks()

    elif (option == 3):
        if not tasks :
            print("There is nothing to mark as compete.")
        else :
            show_tasks()
            try: 
                task_id = int(input("Mark the task as done.")) - 1
                if 0 <= task_id < len(tasks):
                    tasks[task_id] += " ✅"
                    print("Task marked as done!")
                else:
                    print("Invalid option.")

            except ValueError:
                print("choose a valid option.")
                continue

    elif (option == 4):
        if not tasks:
            print("There is nothing to delete in the list")
        else:
            try:
                task_id = int(input("Enter the task you want to delete.")) - 1
                if 0 <= task_id < len(tasks):
                    delete = tasks.pop(task_id)
                    print(f"Deleted: {delete}")
                else:
                    print("Invalid number")

            except ValueError:
                print("choose a valid option")
                continue


    elif( option == 5):
        print("Exiting... Goodbyee")
        break

    else:
        print("Invalid option.Please try again.")