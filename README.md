# TASK02-ELEVATE-LABS-INTERNSHIP
Created to store all the files for Elevate Labs internship Task 2 held on 5th August 2025.

Python CLI based To-Do list manager.

Imports:<br/>
The os module is used to interact with the operating system, mainly to check if files exist.

Function:  create_file(File_Name)<br/>
•	Checks if a file with the given name exists:<br/>
•	If it does, prints a message indicating it already exists.<br/>
•	If not, creates a new empty file with write mode 'w', then confirms creation.

Function:  add_tasks(File_Name)<br/>
•	Checks if the specified file exists:<br/>
•	If not, prompts the user to create it first or use existing file.<br/>
•	Otherwise, prompts the user to input a task, then appends it to the file with a newline.

Function:  edit_tasks(File_Name)<br/>
•	Checks if the file exists:<br/>
•	If not, informs the user.<br/>
•	If it exists, reads all tasks into a list.<br/>
•	Calls view_tasks() to display current tasks.<br/>
•	Prompts the user to specify which task to edit by number.<br/>
•	Validates input: Ensures it's an integer and within valid range.<br/>
•	If valid, prompts for the updated task and replaces the old one.<br/>
•	Saves the updated list back to the file.

Function:  remove_tasks(File_Name)<br/>
•	Similar to editing:<br/>
•	Checks if file exists.<br/>
•	Loads tasks into a list.<br/>
•	Displays current tasks.<br/>
•	Prompts for task number to remove.<br/>
•	Validates input.<br/>
•	Removes the selected task from the list.<br/>
•	Saves the updated list back to the file.

Function:  view_tasks(File_Name)<br/>
•	Checks if the file exists:<br/>
•	If not, informs the user.<br/>
•	If it exists, reads the entire content:<br/>
•	If content is present, displays it.<br/>
•	If empty, indicates the to-do list is empty.<br/>

Function:  main()<br/>
•	Runs an infinite loop to present a menu options include creating a file, adding tasks, editing, removing, viewing, and exiting.<br/>
•	Prompts the user to select an action by number.<br/>
•	Uses try-except to handle invalid (non-integer) inputs gracefully.<br/>
•	Depending on the choice prompts for a filename.<br/>
•	Calls the corresponding function.<br/>
•	Exits the loop if the user chooses to exit.

Overall flow:<br/>
•	User interacts via numbered menu choices.<br/>
•	The program manages tasks stored in text files.<br/>
•	Validates user inputs to prevent errors.<br/>
•	Provides feedback after each operation.<br/>

Summary:<br/>
This script is a simple, file-based To-Do list manager that allows creating files, adding, editing, viewing, and removing tasks, all through a command-line interface with input validation and basic file handling.

Programming language used: Python (Functions, File Handling, Lists)<br/>
Tools: Python IDLE 3.8
