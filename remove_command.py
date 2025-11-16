from datetime import date
from os import path, sep, remove, getcwd
from json import load, dump, decoder
from update_tasker_files import get_tasker_config_file_paths, restore_tasker_file
from config import list_of_notes, list_of_tasks


def remove_task_function(args):

    remove_tasker_list(args, list_of_tasks)

def remove_note_function(args):

    remove_tasker_list(args, list_of_notes)

def remove_file_in_cwd(args, file_name, file_type):
    
    CURRENT_DIRECTORY = getcwd()
    
    PATH_TO_FILE = sep.join([CURRENT_DIRECTORY, f"{file_name}.{file_type}"])

    if not path.exists(PATH_TO_FILE):
        
        user_input=input(f"{file_name}.{file_type} not in current working directory, {CURRENT_DIRETORY}\n So removal is not possible do you still want to remove {file_name} from tasker list? (y/N): ")
        
        while user_input not in ["y", "Y", "n", "N"]:
            user_input = input("Invalid input please try again (y/N): ")

        if user_input.lower() == "n":
            return False

    #Removing file from current directory
    try:
        remove(PATH_TO_FILE)

        if args.verbose:
            print(f"Removed {file_name} in the following directory: {CURRENT_DIRECTORY}")

    except PermissionError as error:
        print(f"Didn't have permission to remove {file_name}: {error}")

    except OSError as error:
        print(f"OS didn't allow for removal of {file_name}: {error}")

    except IsADirectoryError as error:
        print(f"Couldn't remove {file_name} as it seems to be a directory: {error}")

    except Exception as error:
        print(f"Something unexpected happened, {file_name} not removed: {error}")

    return True

def remove_tasker_list(args, list_type):

    #List of tasker paths
    tasker_list_paths = get_tasker_config_file_paths()

    #If path for list type doesn't exist than restore it
    if not path.exists(tasker_list_paths[list_type]):
        restore_tasker_file(args, tasker_list_paths[list_type])

    
    specified_list_path = tasker_list_paths[list_type]
            
    #Opens specified file 
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
    
    files_to_be_removed = set(args.file_names)

    #Removes specified files
    for item in taskers_list.copy():
        if item["file_name"] in files_to_be_removed:

            #Remove file from its directory
            if "file type" in item:
                remove_from_tasker = remove_file_in_cwd(args, item["file_name"], item["file type"])    

                if not remove_from_tasker:
                    continue

            taskers_list.remove(item)
            files_to_be_removed.remove(item["file_name"])
                     

            if args.verbose:
                print(f"Removed {item["file_name"]} from {list_type}")


    
    #Add files back
    try:
        with open(specified_list_path, "w") as file:
            dump(taskers_list, file, indent=6)

            if args.verbose:
                print(f"Successfully removed items from {list_type}")

                if len(files_to_be_removed) != 0:
                    print(f"Files not removed: {files_to_be_removed}")



    except decoder.JSONDecodeError as error:
        print(f"Couldn't copy changes to JSON file: {error}")
        return

    except IOError as error:
        print(f"Couldn't open file to copy changes: {error}")
        return

    except Exception as error:
        print(f"Something unexpected happened: {error}")
        return
