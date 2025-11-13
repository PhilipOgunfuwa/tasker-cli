from datetime import date
from os import path, sep, makedirs
from json import dump, load, decoder

def create_json_file_at_path(given_path, file):

    #Path for file
    path_for_file = f"{given_path}{sep}{file}"

    #Create path if path doesn't exist
    if not path.exists(given_path):

        try:
            makedirs(given_path)

        except OSError as error:
            print(f"Error trying to create task: {error}")
    
    #Dont do anything if file already exists
    if path.isfile(path_for_file):
        raise FileExistsError("File already exist") 

    #Open file at given path
    try:
        with open(path_for_file, "x") as file:
           pass

    #Error trying to open file
    except IOError as error:
        print(f"Error trying to make file: {error}")

    return path_for_file

def add_note_to_list(args, path_to_note):
    """Functin to add note to list of notes for show notes command"""

    #path to tasker notes list
    os_delimiter = sep

    path_to_note_list = os_delimiter.join(["~", ".config", "tasker", "list of notes.json"])
    path_to_tasker = os_delimiter.join(["~", ".config", "tasker"])

    #Expanded path that includes home directory
    expanded_path_to_note_list = path.expanduser(path_to_note_list)
    expanded_path_to_tasker = path.expanduser(path_to_tasker)

    #If no list of notes file then try and make one
    if not path.isfile(expanded_path_to_note_list):
        try:
            create_json_file_at_path(expanded_path_to_tasker, "list of notes.json")
            

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




