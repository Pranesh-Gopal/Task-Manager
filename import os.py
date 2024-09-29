import os

# Task Manager class
class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()  # Load tasks from file on startup

    # Load tasks from the file
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                for line in file:
                    task_name, status = line.strip().split(',')
                    self.tasks.append({"task": task_name, "completed": status == "True"})
        else:
            print("No existing task file found, starting with an empty list.")

    # Save tasks to the file
    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task['task']},{task['completed']}\n")

    # Add a new task
    def add_task(self, task_name):
        self.tasks.append({"task": task_name, "completed": False})
        self.save_tasks()

    # Edit an existing task
    def edit_task(self, task_index, new_task_name):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["task"] = new_task_name
            self.save_tasks()
        else:
            print("Invalid task index.")

    # Delete a task
    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
        else:
            print("Invalid task index.")

    # Mark a task as complete
    def mark_task_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            self.save_tasks()
        else:
            print("Invalid task index.")

    # Display all tasks with their status
    def display_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            print("\nCurrent Tasks:")
            for i, task in enumerate(self.tasks):
                status = "Complete" if task["completed"] else "Incomplete"
                print(f"{i + 1}. {task['task']} [{status}]")

# Main program loop
def main():
    task_manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            task_manager.display_tasks()
        elif choice == "2":
            task_name = input("Enter task name: ")
            task_manager.add_task(task_name)
            print("Task added successfully.")
        elif choice == "3":
            task_manager.display_tasks()
            task_index = int(input("Enter the task number to edit: ")) - 1
            new_task_name = input("Enter new task name: ")
            task_manager.edit_task(task_index, new_task_name)
            print("Task edited successfully.")
        elif choice == "4":
            task_manager.display_tasks()
            task_index = int(input("Enter the task number to delete: ")) - 1
            task_manager.delete_task(task_index)
            print("Task deleted successfully.")
        elif choice == "5":
            task_manager.display_tasks()
            task_index = int(input("Enter the task number to mark as complete: ")) - 1
            task_manager.mark_task_complete(task_index)
            print("Task marked as complete.")
        elif choice == "6":
            print("Exiting the Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
