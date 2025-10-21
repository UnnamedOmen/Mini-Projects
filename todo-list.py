import json

file_name  = 'todo_list.json'

def load_tasks():
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except Exception as e:
        print(e)
        return {"tasks": []}

def save_tasks(tasks):
    try:
        with open(file_name, "w") as file:
            return json.dump(tasks, file)
    except:
        print("Failed to save.")

def view_tasks():
    pass

def create_tasks():
    description = input("Enter the task description:\n")

    if description:
        tasks["taks"].append({"description": description, "complete": False})
        save_tasks(tasks)
        print("Task added")
    else:
        print("Description cannot be empty.")
        
def mark_task_complete():
    pass

def main():
    tasks = load_tasks()
    print(tasks)
    
    
    while True:
        print("\n To-Do Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")
    
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            create_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            print("Goodbye")
            break
        else:
            ("Invalid choice. Please try again.")

main()