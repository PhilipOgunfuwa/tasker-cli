from datetime import date
from os import path, sep, remove
from json import load, dump, decoder

def remove_task_function(args):

    #path to tasker task list
    os_delimiter = sep

    path_to_task_list = os_delimiter.join(["~", ".config", "tasker", "list of tasks.json"])

    #expanded path that includes home directory
    expanded_path_to_task_list = path.expanduser(path_to_task_list)

    #If no task list file do nothing
    if not path.isfile(expanded_path_to_task_list):
        print(f"Didn't remove task because their is no task list @: {expanded_path_to_task_list}")
        return


    #Open task list 
    try:
        with open(expanded_path_to_task_list, "r") as file:
            task_list = load(file)    

    #If empty json file than make empty list
    except decoder.JSONDecodeError: 
        task_list = []

    #Removes tasks named from the arguments
    for task in task_list.copy():
        if task["file_name"] in args.file_names:
            task_list.remove(task)

    #Add task list with removed tasks back
    try:
        with open(expanded_path_to_task_list, "w") as file:
            dump(task_list, file, indent=6, skipkeys=True)

            if args.verbose:
                print(f"Removed the following files {args.file_names}")
                print(f"Now only {len(task_list)} tasks")

    except IOError as error:
        print(f"Couldn't dump to the task file so no changes made: {error}")
        return

    except Exception as error:
        print(f"Something went wrong: {error}")
        return

    
def remove_note_function(args):


    #path to tasker note list
    os_delimiter = sep

    path_to_note_list = os_delimiter.join(["~", ".config", "tasker", "list of notes.json"])

    #expanded path that includes home directory
    expanded_path_to_note_list = path.expanduser(path_to_note_list)

    #If no note list file do nothing
    if not path.isfile(expanded_path_to_note_list):
        print(f"Didn't remove task because their is no task list @: {expanded_path_to_note_list}")
        return


    #Open note list 
    try:
        with open(expanded_path_to_note_list, "r") as file:
            note_list = load(file)    

    #If empty json file than make empty list
    except decoder.JSONDecodeError: 
        note_list = {}

    except Exception as error:
        print(f"Something went wrong please try again: {error}")
        return

    #Removes notes  named from the arguments
    for note_path, note in note_list.copy().items():

        #if file name or path of note given remove the note
        if note["file_name"] in args.file_names or note_path in args.file_paths:

            #Remove note from note_path 
            try:
                remove(note_path)

            except Exception as error:
                print(f"Something went horribly wrong aborting operation: {error}")
                return

            #Remove note from json list
            note_list.pop(note_path)
            
            if args.verbose:
                print(f"Removed {note} from list of tasker notes, and from list of tasker notes")

        

    #Add task list with removed tasks back
    try:
        with open(expanded_path_to_note_list, "w") as file:
            dump(note_list, file, indent=6, skipkeys=True)

            if args.verbose:
                print(f"Removed the following files {args.file_names}")
                print(f"Now only {len(note_list)} tasks")

    except IOError as error:
        print(f"Couldn't dump to the task file so no changes made: {error}")
        return

    except Exception as error:
        print(f"Something went wrong: {error}")
        return

