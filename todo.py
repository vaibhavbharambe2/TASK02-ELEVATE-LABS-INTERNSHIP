import os

def create_file(File_Name):
    if os.path.exists(File_Name):
        print(File_Name, "already exists! \n")
    else:
        with open(File_Name, 'w') as myfile:
            print(File_Name, "created. \n")
            
def add_tasks(File_Name):
    if not os.path.exists(File_Name):
        print("==> File not found. Please create a file first or use existing. \n")
        return
    else:
        User_Input = input("Enter tasks one at a time: ").strip()

        with open(File_Name, 'a') as myfile:
            myfile.write(User_Input + "\n")

        print("==> Tasks added in file. \n")


def edit_tasks(File_Name):
    if not os.path.exists(File_Name):
        print(f"==> File '{File_Name}' does not exists! \n")
    else:

        tasks = []

        with open(File_Name, 'r') as myfile:
            tasks = myfile.readlines()

        view_tasks(File_Name)

        if not tasks:
            print("==> There are no tasks to edit. \n")
        else:
            try:
                edit_index = int(input("Enter task number to edit: "))

                if edit_index < 1 or edit_index > len(tasks):
                    print("==> Invalid task number. Try again. \n")
                    return
                else:

                    updated_task = input("Enter upadted task: ")

                    tasks[edit_index - 1] = updated_task + "\n"

                    with open(File_Name, 'w') as myfile:
                        myfile.writelines(tasks)

                    print("Task Updated! \n")
                    
            except ValueError:
                print("==> Invalid task number. Try again. \n")


def remove_tasks(File_Name):
    if not os.path.exists(File_Name):
        print(f"==> File '{File_Name}' does not exists! \n")
    else:

        tasks = []

        with open(File_Name, 'r') as myfile:
            tasks = myfile.readlines()

        view_tasks(File_Name)

        if not tasks:
            print("==> There are no tasks to remove. \n")
        else:
            try:
                remove_index = int(input("Enter task number to remove: "))

                if remove_index < 1 or remove_index > len(tasks):
                    print("==> Invalid task number. Try again. \n")
                    return
                else:
                    tasks.pop(remove_index - 1)

                    with open(File_Name, 'w') as myfile:
                        myfile.writelines(tasks)

                    print("Task Removed! \n")

            except ValueError:
                print("==> Invalid task number. Try again. \n")
                
    
def view_tasks(File_Name):
    if not os.path.exists(File_Name):
        print(f"==> File '{File_Name}' does not exists! \n")
    else:
        with open(File_Name, 'r') as myfile:
            content = myfile.read()

        if content:
            print(content)
            print()
        else:
            print("==> To-Do list is empty. \n")


def main():
    
    while True:

        print("** Welcome to To-Do list ** \n")
        print("Select your action from below list:\n")
        print("1. Create a To-Do file")
        print("2. Add tasks")
        print("3. Edit tasks")
        print("4. Remove tasks")
        print("5. View tasks")
        print("6. Exit")
        print()

        try:
            User_Choice = int(input("Enter your Choice. Please enter number specified against the action: "))
        except ValueError:
            print("==> Invalid input. Please enter between 1 to 6. \n")
            continue

        print()

        if User_Choice == 6:
            print("Exiting To-Do list... \n")
            break

        elif User_Choice >= 1 and User_Choice <= 6:

            File_Name = input("Enter file name with '.txt' extension: ")

            if User_Choice == 1:
                create_file(File_Name)
            elif User_Choice == 2:
                add_tasks(File_Name)
            elif User_Choice == 3:
                edit_tasks(File_Name)
            elif User_Choice == 4:
                remove_tasks(File_Name)
            elif User_Choice == 5:
                view_tasks(File_Name)
            elif User_Choice == 6:
                print("Exiting To-Do list... \n")
                break
            else:
                print("==> Invalid input. Please enter between 1 to 6. \n")

        else:
            print("==> Invalid input. Please enter between 1 to 6. \n")


main()
