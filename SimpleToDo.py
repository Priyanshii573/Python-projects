class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def delete_task(self, index):
        del self.tasks[index]

    def mark_completed(self, index):
        self.tasks[index]["completed"] = True

    def display_tasks(self):
        print("\nTo-Do List:")
        for i, task in enumerate(self.tasks):
            status = " [X]" if task["completed"] else " [ ]"
            print(f"{i + 1}. {task['task']}{status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "3":
            index = int(input("Enter the task number to mark as completed: ")) - 1
            todo_list.mark_completed(index)
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
