import os
def Main():
    # Open File (Make Or Read), find out if I am reading an old file, or creating a new file.
    fName, exists= OpenFile()

    # See if it's a new file or not
    if exists == 'yes':

        # See if they want to see, add or edit tasks
        while True:
            wtd = WhatToDo()
            if wtd == 'see':
                with open(fName,'r') as f:
                    f.seek(0)
                    print('\n')
                    print(f.read())
            elif wtd == 'add':
                AddToDo(fName)
            elif wtd == 'edit':
                EditTasks(fName)
            elif wtd == 'done':
                break
        f.close()

        # Close file when done
    if exists == 'no':
        # Double check that they meant to create a new file
        yOrN = input("The file you wanted did not exists, so it has been created, do you wish to create a new file? \nYes I do 'yes'. \nNo I do not 'no'. \n").lower().strip()
        # If yes, then:
        if yOrN == 'yes':
                # Add tasks
            AddToDo(fName)
                # See tasks once done making them
            with open(fName,'r') as f:
                print(f.read())
                    # Then see if they want to add, see, or edit tasks
                while True:
                    wtd = WhatToDo()
                    try:
                        if wtd == 'see':
                            f.seek(0)
                            print('\n')
                            print(f.read())
                        elif wtd == 'add':
                            AddToDo(fName)
                        elif wtd == 'edit':
                            EditTasks(fName)
                        elif wtd == 'done':
                            break
                    except:
                        print("Please enter an actual command. Or make sure that you spelled correctly.")
            # If no, then:
        elif yOrN == 'no':
                # Print what might've happend, and see if want to delete file
            print("This might have happened because of a miss-type, or becuase the file you wanted is not in this folder.")
            os.remove(fName)
            print("The file has been deleted.")
            Main()
        else:
            print("Incompatible answer. Deleting file.")
            os.remove(fName)
            print("The file has been deleted.")
            Main()

def OpenFile():
    fName = input("Please enter the file name, or a new name if you wish to create a file: ").strip()
    try:
        with open(fName, "r") as f:
            exists = 'yes'
    except FileNotFoundError:
        with open(fName, "x") as f:
            exists = 'no'
    return fName, exists

def WhatToDo():
    wtd = input("\nPlease enter if you would like to: \nSee your tasks 'see'. \nAdd to your tasks 'add'. \nEdit/Finish existing tasks 'edit'. \nDone with To-Do List 'done'.\n")
    return wtd.lower().strip()

def AddToDo(fName):
    with open(fName, "a") as f:
        while True:
            task = input("Please enter a task you would like to add (or 'done'): ").strip()
            if task.lower() != 'done':
                f.write(task + '\n')
            else:
                break
    return

def EditTasks(fName):
    tEdit = input("What task would you like to edit? (or 'nm' to cancel)\n")
    if tEdit.lower().strip() == 'nm':
        return
    with open(fName, "r") as f:
        for lineNumber, line in enumerate(f, start=1):
            if tEdit in line:
                lNum = lineNumber
    dOrE = input ("\nWhat would you like to do with this task: \nDelete it 'delete'. \nEdit it 'edit'. \nNevermind 'nm'. \n").lower().strip()
    if dOrE == 'delete':
        DelOrEdit(fName, lNum, 'd')
        return
    elif dOrE == 'edit':
        DelOrEdit(fName, lNum, 'e')
        return
    elif dOrE == 'nm':
        return
    
def DelOrEdit(fName, lNum, dOrE):
    # Fill it out
    if dOrE == 'd':
        # Delete the task
        with open(fName, "r") as f:
            lines = f.readlines()
        del lines[lNum - 1]
        with open(fName, "w") as f:
            f.writelines(lines)
        return
    elif dOrE == 'e':
        newLine = input("What would you like to change this task to? \n")
        with open(fName, "r") as f:
            lines = f.readlines()
        index = lNum - 1
        if not (0 <= index < len(lines)):
            raise ValueError("Line number out of range")
        lines[index] = newLine + "\n"
        with open(fName, "w") as f:
            f.writelines(lines)
        return

Main()