tasks = []

def add_task():
    title = input("Enter task title: ")
    deadline = input("Enter deadline (e.g., 2024-11-17): ")
    priority = input("Enter priority (High, Medium, Low): ")
    tasks.append({"title": title, "deadline": deadline, "priority": priority, "completed": False})
    print("Task added successfully!")

def view_tasks():
    for i, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{i}. {task['title']} | {task['deadline']} | {task['priority']} | {status}")

def complete_task():
    task_id = int(input("Enter task number to mark as completed: "))
    if 1 <= task_id <= len(tasks):
        tasks[task_id - 1]["completed"] = True
        print("Task marked as completed!")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            break
        else:
            print("Invalid choice, try again.")

main()