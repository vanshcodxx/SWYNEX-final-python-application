
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks():
    """Load saved tasks from the JSON file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Warning: Invalid task data. Starting with an empty list.")
            return []

        return data

    except (json.JSONDecodeError, OSError) as error:
        print(f"Warning: Could not load tasks: {error}")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True

    except (OSError, TypeError, ValueError) as error:
        print(f"Error saving tasks: {error}")
        return False


def get_next_id(tasks):
    """Generate the next available task ID."""
    valid_ids = [
        task["id"]
        for task in tasks
        if isinstance(task, dict)
        and isinstance(task.get("id"), int)
        and not isinstance(task.get("id"), bool)
    ]
    return max(valid_ids, default=0) + 1


def add_task(tasks):
    title = input("Enter task title: ").strip()

    if not title:
        print("Error: Task title cannot be empty.")
        return

    task = {
        "id": get_next_id(tasks),
        "title": title,
        "completed": False
    }

    updated_tasks = tasks + [task]

    if save_tasks(updated_tasks):
        tasks.append(task)
        print(f"Task added successfully! ID: {task['id']}")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found. Add your first task!")
        return

    print("\n--- YOUR TASKS ---")

    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['id']}. {task['title']} [{status}]")


def complete_task(tasks):
    task_id = input("Enter task ID to complete: ").strip()

    if not task_id.isdigit() or int(task_id) <= 0:
        print("Error: Enter a valid positive task ID.")
        return

    task_id = int(task_id)

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("This task is already completed.")
                return

            updated_tasks = [
                {**item, "completed": True}
                if item["id"] == task_id else item
                for item in tasks
            ]

            if save_tasks(updated_tasks):
                task["completed"] = True
                print("Task marked as completed!")
            return

    print("Error: Task ID not found.")


def delete_task(tasks):
    task_id = input("Enter task ID to delete: ").strip()

    if not task_id.isdigit() or int(task_id) <= 0:
        print("Error: Enter a valid positive task ID.")
        return

    task_id = int(task_id)

    if not any(task["id"] == task_id for task in tasks):
        print("Error: Task ID not found.")
        return

    updated_tasks = [
        task for task in tasks
        if task["id"] != task_id
    ]

    if save_tasks(updated_tasks):
        tasks[:] = updated_tasks
        print("Task deleted successfully!")
