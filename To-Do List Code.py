import os
def Main():
    # Open File (Make Or Read), find out if I am reading an old file, or creating a new file.
    f, exists= OpenFile()

    # See if it's a new file or not
    if exists == 'yes':

        # See if they want to see, add or edit tasks
        while True:
            wtd = WhatToDo()
            if wtd == 'see':
                print('\n')
                print(f.read())
            elif wtd == 'add':
                AddToDo(f)
            elif wtd == 'edit':
                EditTasks(f)
            elif wtd == 'done':
                break
        f.close()

        # Close file when done
    if exists == 'no':
        # Double check that they meant to create a new file
        yOrN = input("The file you wanted did not exists, so it has been created, did you want to create a new file? \nYes I did 'yes'. \nNo I did not 'no'. \n").lower().strip()
        # If yes, then:
        if yOrN == 'yes':
                # Add tasks
            AddToDo(f)
                # See tasks once done making them
            f = open(f.name ,'r')
            print(f.read())
                # Then see if they want to add, see, or edit tasks
            while True:
                wtd = WhatToDo()
                try:
                    if wtd == 'see':
                        print('\n')
                        print(f.read())
                    elif wtd == 'add':
                        AddToDo(f)
                    elif wtd == 'edit':
                        EditTasks(f)
                    elif wtd == 'done':
                        break
                except:
                    print("Please enter an actual command. Or make sure that you spelled correctly.")
                # Close file when done
            f.close()
            # If no, then:
        elif yOrN == 'no':
                # Print what might've happend, and see if want to delete file
            print("This might have happened because of a miss-type, or becuase the file you wanted is not in this folder.")
            os.remove(f.name)
            print("The file has been deleted.")
            Main()
        else:
            print("Incompatible answer. Deleting file.")
            os.remove(f.name)
            print("The file has been deleted.")
            Main()

def OpenFile():
    fName = input("Please enter the file name, or a new name if you wish to create a file: ").strip()
    try:
        f = open(fName,"r")
        exists = 'yes'
    except FileNotFoundError:
        f = open(fName,"x")
        exists = 'no'
    return f, exists

def WhatToDo():
    wtd = input("\nPlease enter if you would like to: \nSee your tasks 'see'. \nAdd to your tasks 'add'. \nEdit/Finish existing tasks 'edit'. \nDone with To-Do List 'done'.\n")
    return wtd.lower().strip()

def ReadToWrite(f):
    fName = f.name
    f.close()
    f = open(fName,'a')
    return f

def AddToDo(f):
    f = ReadToWrite(f)
    while True:
        task = input("Please enter a task you would like to add (or 'done'): ")
        if task.lower().strip() != 'done':
            f.write(task.strip() + '\n')
        else:
            break
    f = WriteToRead(f)
    return

def WriteToRead(f):
    fName = f.name
    f.close()
    f = open(fName,'r')
    return f

def EditTasks(f):
    tEdit = input("What task would you like to edit? (or 'nm' to cancel)\n")
    if tEdit.lower().strip() == 'nm':
        f = open(f.name,'r')
        return
    for lineNumber, line in enumerate(f, start=1):
        if tEdit in line:
            lNum = lineNumber
    dOrE = input ("What would you like to do with this task: \nDelete it 'delete'. \nEdit it 'edit'. \nNevermind 'nm'. \n").lower().strip()
    if dOrE == 'delete':
        DelOrEdit(f, lNum, 'd')
        return
    elif dOrE == 'edit':
        DelOrEdit(f, lNum, 'e')
        return
    elif dOrE == 'nm':
        f = open(f.name,'r')
        return
    
def DelOrEdit(f, lNum, dOrE):
    # Fill it out
    if dOrE == 'd':
        # Delete the task
        with open(f.name, "r") as f:
            lines = f.readlines()
        del lines[lNum - 1]
        with open(f.name, "w") as f:
            f.writelines(lines)
        WriteToRead(f)
        return
    elif dOrE == 'e':
        newLine = input("What would you like to change this task to? \n")
        with open(f.name, "r") as f:
            lines = f.readlines()
        index = lNum - 1
        if not (0 <= index < len(lines)):
            raise ValueError("Line number out of range")
        lines[index] = newLine + "\n"
        with open(f.name, "w") as f:
            f.writelines(lines)
        return

Main()