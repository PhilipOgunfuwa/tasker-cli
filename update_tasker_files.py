from datetime import date
from os import path, sep, makedirs
from json import dump, load, decoder

def create_file_at_tasker(file):

    os_delimiter = sep

    #path for tasker
    path_to_tasker = os_delimiter.join(["~", ".config", "tasker"])
    expanded_path_to_tasker = path.expanduser(path_to_tasker)

    #Path for file
    path_to_file = os_delimiter.join([path_to_tasker, file])
    expanded_path_to_file = path.expanduser(path_to_file)

    #Create path if path doesn't exist
    if not path.exists(expanded_path_to_tasker):

        try:
            makedirs(expanded_path_to_tasker)

        except OSError as error:
            print(f"Error trying to create task: {error}")
    
    #Dont do anything if file already exists
    if path.isfile(expanded_path_to_file):
        return

    #Open file at given path
    try:
        with open(expanded_path_to_file, "x") as file:
           pass

    #Error trying to open file
    except IOError as error:
        print(f"Error trying to make file: {error}")

    return expanded_path_to_file

def add_task_to_list(args, task_attributes):
    """Function to add task to list of tasks for show tasks command"""

    #path to tasker task list
    os_delimiter = sep

    path_to_task_list = os_delimiter.join(["~", ".config", "tasker", "list of tasks.json"])

    #expanded path that includes home directory
    expanded_path_to_task_list = path.expanduser(path_to_task_list)

    #If no list of task file then try and make one
    if not path.isfile(expanded_path_to_task_list):

        try:
            create_file_at_tasker("list of tasks.json")

        except Exception as error:
            print(f"Something went wrong: {error}")
            return

    
    #Opens list of tasks
    try:
        with open(expanded_path_to_task_list, "r") as file:
            list_of_tasks = load(file)

    #File is empty make json dictionary
    except decoder.JSONDecodeError:
        list_of_tasks = []

    except Exception as error:
        print(f"Something went wrong: {error}\n Couldn't add note to list of notes BE CAUTIOUS")
        return

    #Makes path to note the key and then item the notes attributes
    list_of_tasks.append(task_attributes)

    
    with open(expanded_path_to_task_list, "w") as file:
        dump(list_of_tasks, file, indent=6, skipkeys=True)

        #Explain what happened to user
        if args.verbose:
            print(f"Added task to list of tasks  @ {expanded_path_to_task_list}")


    
def add_note_to_list(args, path_to_note):
    """Functin to add note to list of notes for show notes command"""

    #path to tasker notes list
    os_delimiter = sep

    path_to_note_list = os_delimiter.join(["~", ".config", "tasker", "list of notes.json"])

    #Expanded path that includes home directory
    expanded_path_to_note_list = path.expanduser(path_to_note_list)

    #If no list of notes file then try and make one
    if not path.isfile(expanded_path_to_note_list):
        try:
            create_file_at_tasker("list of notes.json")

        except Exception as error:
            print(f"Something went wrong: {error}")
            return 



    #Opens list of notes
    try:
        with open(expanded_path_to_note_list, "r") as file:
            list_of_notes = load(file)

    #File is empty make json dictionary
    except decoder.JSONDecodeError:
        list_of_notes = {}

    except Exception as error:
        print(f"Something went wrong: {error}\n Couldn't add note to list of notes BE CAUTIOUS")
        return

    #Empty list to hold attributes of note
    note_attributes = {}
    
    #Creates JSON object for args attributes
    for variable_name, content in vars(args).items():
        
        #If instance is a callable method or function or a boolean don't add to attributes
        if hasattr(content, "__call__") or isinstance(content, bool):
            continue
        
        #If content is a date type than make it a string
        if isinstance(content, date):
            content = content.strftime("%Y-%m-%d")

        note_attributes[variable_name] = content            

    #Makes path to note the key and then item the notes attributes
    list_of_notes[path_to_note] = note_attributes

    
    with open(expanded_path_to_note_list, "w") as file:
        dump(list_of_notes, file, indent=6, skipkeys=True)

        #Explain what happened to user
        if args.verbose:
            print(f"Added notes to list of notes @ {expanded_path_to_note_list}")




