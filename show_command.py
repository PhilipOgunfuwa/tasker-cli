from json import load, dumps, decoder
from os import path, sep
from update_tasker_files import create_file_at_tasker

def show_task_function(args):

    
    #path to tasker task list
    os_delimiter = sep

    path_to_task_list = os_delimiter.join(["~", ".config", "tasker", "list of tasks.json"])

    #expanded path that includes home directory
    expanded_path_to_task_list = path.expanduser(path_to_task_list)

    #If no list of task file then try and make one
    if not path.isfile(expanded_path_to_task_list):

        try:
            create_file_at_tasker("list of tasks.json")

            if args.verbose:
                print(f"Created list of tasks json file at {expanded_path_to_task_list}")

        except Exception as error:
            print(f"Something went wrong: {error}")
            return

    
    #Opens list of tasks
    try:
        with open(expanded_path_to_task_list, "r") as file:
            list_of_tasks = load(file)

    #File is empty make json dictionary
    except decoder.JSONDecodeError:
        print(f"Couldn't open list of tasks b/c it was empty json")
        return

    except Exception as error:
        print(f"Something went wrong: {error}\n Couldn't add note to list of notes BE CAUTIOUS")
        return


   
    if args.show_all:
        print(dumps(list_of_tasks, indent=6, skipkeys=True))
        return

    for task in list_of_tasks:
        if task["file_name"] in args.file_names:
            print(dumps(task, indent=6, skipkeys=True))
            print()

            

def show_note_function(args):

    
    #path to tasker note list
    os_delimiter = sep

    path_to_notes_list = os_delimiter.join(["~", ".config", "tasker", "list of notes.json"])

    #expanded path that includes home directory
    expanded_path_to_notes_list = path.expanduser(path_to_notes_list)

    #If no list of note file then try and make one
    if not path.isfile(expanded_path_to_notes_list):

        try:
            create_file_at_tasker("list of notes.json")

            if args.verbose:
                print(f"Created list of tasks json file at {expanded_path_to_notes_list}")

        except Exception as error:
            print(f"Something went wrong: {error}")
            return

    
    #Opens list of tasks
    try:
        with open(expanded_path_to_notes_list, "r") as file:
            list_of_notes = load(file)

    #File is empty make json dictionary
    except decoder.JSONDecodeError:
        print(f"Couldn't open list of tasks b/c it was empty json")
        return

    except Exception as error:
        print(f"Something went wrong: {error}\n Couldn't add note to list of notes BE CAUTIOUS")
        return


   
    if args.show_all:
        print(dumps(list_of_notes, indent=6, skipkeys=True))
        return

    for note_path, note in list_of_notes.copy().items():
        if note["file_name"] in args.file_names or note_path in args.file_paths:
            print(dumps(list_of_notes[note_path], indent=6, skipkeys=True))
            print()

