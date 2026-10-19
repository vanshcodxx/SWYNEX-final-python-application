
# SWYNEX Final Python Application
## Student Task Manager

### Project Overview
Student Task Manager is a command-line Python application
that helps students manage their daily tasks.

Users can add tasks, view saved tasks, mark tasks as
completed, and delete tasks.

### Features
- Add a task with a title
- View all saved tasks
- Mark a task as completed
- Delete a task by ID
- Validate user input
- Handle invalid task IDs
- Save tasks in a JSON file
- Handle common file and data errors

### Technologies Used
- Python 3
- JSON
- pathlib
- Python standard library

### Project Structure
SWYNEX-Final-Python-Application/
- main.py
- task_manager.py
- tasks.json (created automatically)
- requirements.txt
- README.md
- .gitignore

### Requirements
- Python 3 installed
- Visual Studio Code or another code editor

No external packages are required.

### How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open a terminal in the project directory.
4. Run the following command:

   python main.py

### How to Use
1. Select Add Task to create a task.
2. Select View Tasks to see all tasks.
3. Select Mark Task as Completed and enter its ID.
4. Select Delete Task and enter its ID to remove it.
5. Select Exit to close the application.

### Data Storage
Tasks are saved in tasks.json.
The data remains available after restarting the application.

### Validation and Error Handling
- Empty task titles are rejected.
- Invalid menu choices are handled.
- Invalid task IDs are rejected.
- Missing or unreadable task data is handled.
- File saving errors are reported to the user.

### Testing
Test the application by adding, viewing, completing,
and deleting tasks. Also test invalid menu choices,
empty titles, and nonexistent task IDs.

### Learning Outcomes
This project helped me practise Python functions,
modules, loops, conditional statements, JSON file handling,
input validation, and exception handling.

### Internship
Developed as Task 4 of the SWYNEX Python Internship.
