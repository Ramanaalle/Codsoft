import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.tasks = []
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_task_button = tk.Button(root, text="Add  Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, width=60, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_task_button = tk.Button(root, text="Complete Task", command=self.cmplt_task)
        self.complete_task_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_task_button = tk.Button(root, text="Delete Task", command=self.dlt_task)
        self.delete_task_button.grid(row=2, column=1, padx=10, pady=10)
        self.refresh_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.refresh_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def refresh_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "○"
            self.task_listbox.insert(tk.END, f"{index}. [{status}] {task['task']}")

    def cmplt_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.refresh_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def dlt_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.refresh_list()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
