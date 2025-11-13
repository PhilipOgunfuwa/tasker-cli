from datetime import date
from json import dump 
from os import path, sep
from update_command import create_json_file_at_path, add_note_to_list
    
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
            file.write(f"\nDESCRIPTION: {args.description}")
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

    #Os specific delimiter "/" or "\"
    os_delimiter = sep

    #Path for tasker tasks folder
    tasks_directory_path = os_delimiter.join(["~", ".config", "tasker", "tasks"])

    #Path for tasker including home directory
    expanded_path = path.expanduser(tasks_directory_path)

    #json file for task
    json_file = f"{args.file_name}.json" 

    #Empty dictionary that holds task attributes
    task_attributes = {}

    for variable_name, content in vars(args).items():
        
        #If content is a callable method, function, or a boolean don't add to attributes of task
        if hasattr(content, "__call__") or isinstance(content, bool):
            continue

        #If content is a date type than make it a string
        if isinstance(content, date):
            content = content.strftime("%Y-%m-%d")

        task_attributes[variable_name] = content
    #Create file
    try:
        task_path = create_json_file_at_path(expanded_path, json_file)

    except FileExistsError as error:
        print(f"Error trying to create task: {error}")
        return

    except Exception as error:
        print(f"Something else went wrong please try again: {error}")
        return

    #Dumping arguments in Json file
    try:
        with open(task_path, "w") as file:
            dump(task_attributes, file, indent=6, skipkeys=True)
            
            if args.verbose:
                print(f"Creating task: {args.file_name}")
            
    
    except IOError as error:
        print(f"Error when trying to open task: {error}")

def create_task_group_function(args):
    pass


