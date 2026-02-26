def Main():
    # Open File (Make Or Read), find out if I am reading an old file, or creating a new file.
    f, exists= OpenFile()

    # See if it's a new file or not
    if exists == 'yes':

        # See if they want to add, see, or edit tasks
        while True:
            wtd = WhatToDo()
            if wtd == 'see':
                print(f.read())
            elif wtd == 'add':
                AddToDo(f)
            elif wtd == 'edit':
                EditTasks(f)

        # Close file when done
    if exists == 'no':
        # Double check that they meant to create a new file
        # If yes, then:
            # Add tasks
            # See tasks once done making them
            # Then see if they want to add, see, or edit tasks
            # Close file when done
        # If no, then:
            # Print what might've happend, and see if want to delete file


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
    wtd = input("Please enter if you would like to: \nSee your tasks 'see'. \nAdd to your tasks 'add'. \nEdit/Finish existing tasks 'edit. \nDone with To-Do List 'done'.\n")
    return wtd.lower()

def ReadToWrite(f):
    fName = f.name()
    f.close()
    f = open(fName,'a')
    return f

def AddToDo(f):
    f = ReadToWrite(f)
    while True:
        task = input("Please enter a task you would like to add 'Unload the dishes' (or 'done'): ")
        if task.lower().strip() != 'done':
            f.write(task.strip())
        else:
            break
    f = WriteToRead(f)
    return

def WriteToRead(f):
    fName = f.name()
    f.close()
    f = open(fName,'r')
    return f

def EditTasks(f):
    tEdit = input("What task would you like to edit? \n")
    for lineNumber, line in enumerate(f, start=1):
        if tEdit in line:
            lNum = lineNumber