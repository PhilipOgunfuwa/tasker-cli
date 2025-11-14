from datetime import date
from json import dump 
from os import path, sep
from update_tasker_files import create_file_at_tasker, add_note_to_list, add_task_to_list
    
def create_note_function(args):
    """Function to create org mode file based on the arguments given"""

    #Org mode file name
    note_name = f"{args.file_name}.org"

    #If org mode file exists asks if they want to overwrite or note
    if path.exists(note_name):
        print(f"{note_name} already exists in current working directory")
        user_input = input("Would you like to overwrite this file? (y/N) >> ") 
       
        #Keep prompting user for yes or no
        while user_input not in ["y", "Y", "n", "N"]:
            user_input = input("Didn't understand input please try again. (y/N) >> ")

        #If no stop
        if user_input.lower() == "n":
            return

    #create org mode file based off name
    try:
        with open(note_name, "w") as file:
            #writing property stuff to file

            file.write(f"* Properties\n")
            file.write("\n:PROPERTIES:")
            file.write(f"\n:CLASS: {args.class_name}")
            file.write(f"\n:TYPE: {args.creation_type}")
            file.write(f"\n:DESCRIPTION: {args.description}")
            file.write(f"\n:STARTED: <{args.date_assigned}>")
            file.write(f"\n:DEADLINE: <{args.due_date}>\n")
            file.write(f"* ")

            #Only prints out feedback if user uses -q argument
            if args.verbose:
                print(f"Created org file: {note_name}")
                
            #Adding note to list of notes and their paths etc...
            path_to_note = path.abspath(file.name)

            add_note_to_list(args, path_to_note)

    except IOError as error:
        print(f"Error when trying to open file: {error}")


def create_task_function(args):
    """Function to create a task by adding it to a json file"""

    #Empty dictionary that holds the attributes of the task
    task_attributes = {}

    #Adding JSON serializable objects to task_attributes
    for variable_name, content in vars(args).items():
        
        #If content is a callable method, function, or a boolean don't add to attributes of task
        if hasattr(content, "__call__") or isinstance(content, bool):
            continue

        #If content is a date type than make it a string
        if isinstance(content, date):
            content = content.strftime("%Y-%m-%d")

        task_attributes[variable_name] = content
      
    try:
       #add task to list
       add_task_to_list(args, task_attributes)

    except IOError:
       print(f"Error when trying to open file: {error}")

     




