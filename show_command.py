from json import load, dumps, decoder
from os import path, sep
from update_tasker_files import get_tasker_config_file_paths, restore_tasker_file

def show_task_function(args):

    show_tasker_list(args, "list of tasks")

def show_note_function(args):

    show_tasker_list(args, "list of notes")

def show_tasker_list(args, list_type):

    #List of tasker paths
    tasker_list_paths = get_tasker_config_file_paths()

    #If path for list type doesn't exist than restore it
    if not path.exists(tasker_list_paths[list_type]):
        restore_tasker_file(args, tasker_list_paths[list_type])

    
    specified_list_path = tasker_list_paths[list_type]
            
    try:
        with open(specified_list_path, "r") as file:
            taskers_list = load(file)

            if args.verbose:
                print(f"Successfully opened {list_type}")

    except decoder.JSONDecodeError as error:
        print(f"Couldn't open JSON file: {error}")
        return

    except IOError as error:
        print(f"Couldn't open file: {error}")
        return

    except Exception as error:
        print(f"Something unexpected happened: {error}")
        return

    if args.show_all:
        print(dumps(taskers_list, indent=6))

    else:
        for item in taskers_list:
            if item["file_name"] in args.file_names:
                print(dumps(item, indent=6))
