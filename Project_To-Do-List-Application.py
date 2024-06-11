def display_menu():
    print("Welcome to the To-Do List!/n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_tasks(tasks):
    task_title = input("Enter the task title:")
    tasks.append({"title": task_title, "status": "Incomplete"})
    print(f"Taks '{task_title}' added successfully")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['title']} ({task['status']})")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to mark as complete: ")) - 1
        tasks[task_index]["status"] = "complete"
        print(f"Task '{tasks[task_index]['title']}' marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1 
        delete_task = tasks.pop(task_index)
        print(f"Task '{delete_task['title']}' deleted successfully.")
    except (ValueError, IndexError):
        print("Invalid task number. Please try again.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            add_tasks(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()