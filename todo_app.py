from datetime import datetime
import json

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def add_task(self, description):
        """Add a new task"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.tasks.append(task)
        self.save_task()
        print(f"Task '{description}' added successfully!")

    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found!")
            return

        print("\nYour To-Do List: ")
        print("-" * 50)
        
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            # 1. [ ] Build todo list app
            # 2. [✓] Read book about python
            print(f"{task['id']}. [{status}] {task['description']}")
        print("-" * 50)

    def complete_task(self, task_id):
        """Mark a task as completed"""
        # 1. Loop through tasks property
        # 2. check for task_id
        # 3. mark task['completed'] = true
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_task()
                print(f"Task {task_id} marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")

    def delete_task(self, task_id):
        """Delete a task"""
        # 1. Loop through tasks property
        # 2. Check for task_id in tasks property
        # 3. remove task 
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_task()
                print(f"Task {task_id} deleted!")
                return
        print(f"Task with ID {task_id} not found!")

    def save_task(self):
        """Save tasks to file"""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)
    
    def load_tasks(self):
        """Load tasks from file if it exists"""
        try:
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

def main():
    todo = TodoList()

    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add task")
        print("2. View task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            todo.add_task(description=description)
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo.complete_task(task_id=task_id)
            except ValueError:
                print("Please enter a valid task ID!")
        elif choice == '4':
            todo.view_tasks()
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo.delete_task(task_id=task_id)
            except ValueError:
                print("Please enter a valid task ID!")
        elif choice == '5':
            print("Thank you for using the To-Do List Application!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
