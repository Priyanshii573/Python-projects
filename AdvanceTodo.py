import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.load_tasks()

        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(root, textvariable=self.task_var, font=("Helvetica", 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, font=("Helvetica", 12))
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, font=("Helvetica", 14), selectmode=tk.SINGLE, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task, font=("Helvetica", 12))
        self.delete_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.mark_completed_button = tk.Button(root, text="Mark Completed", command=self.mark_completed, font=("Helvetica", 12))
        self.mark_completed_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

        self.filter_var = tk.StringVar()
        self.filter_var.set("All")
        self.filter_optionmenu = tk.OptionMenu(root, self.filter_var, "All", "Completed", "Incomplete", command=self.filter_tasks)
        self.filter_optionmenu.config(font=("Helvetica", 12))
        self.filter_optionmenu.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        self.sort_button = tk.Button(root, text="Sort by Priority", command=self.sort_tasks, font=("Helvetica", 12))
        self.sort_button.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.save_tasks()
            self.update_task_listbox()
            self.task_var.set("")
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def mark_completed(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["completed"] = True
            self.save_tasks()
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark as completed.")

    def filter_tasks(self, option):
        if option == "All":
            self.update_task_listbox()
        elif option == "Completed":
            filtered_tasks = [task["task"] for task in self.tasks if task["completed"]]
            self.task_listbox.delete(0, tk.END)
            for task in filtered_tasks:
                self.task_listbox.insert(tk.END, task)
        elif option == "Incomplete":
            filtered_tasks = [task["task"] for task in self.tasks if not task["completed"]]
            self.task_listbox.delete(0, tk.END)
            for task in filtered_tasks:
                self.task_listbox.insert(tk.END, task)

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: x["completed"])
        self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = " [X]" if task["completed"] else " [ ]"
            self.task_listbox.insert(tk.END, task["task"] + status)

    def save_tasks(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task["task"] + "," + str(task["completed"]) + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    task, completed = line.strip().split(",")
                    self.tasks.append({"task": task, "completed": bool(completed == "True")})
            self.update_task_listbox()
        except FileNotFoundError:
            pass

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
