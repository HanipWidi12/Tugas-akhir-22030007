import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            del self.tasks[task_index]
            self.update_task_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task.")

    def mark_as_complete(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.tasks[task_index] = self.tasks[task_index] + " (Completed)"
            self.update_task_listbox()
        except:
            messagebox.showwarning("Warning", "You must select a task.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()