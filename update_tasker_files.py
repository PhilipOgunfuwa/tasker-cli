from datetime import date
from os import path, sep, makedirs
from json import dump, load, decoder
from config import tasker_config, list_of_notes, list_of_tasks


def add_to_tasker_list(args, type_attributes, list_type):
    """Function to add task to list of tasks for show tasks command"""

    #List of tasker paths
    tasker_list_paths = get_tasker_config_file_paths()

    #If path for list type doesn't exist than restore it
    if not path.exists(tasker_list_paths[list_type]):
        restore_tasker_file(args, tasker_list_paths[list_type])

    
    specified_list_path = tasker_list_paths[list_type]

    
    #Load specifid JSON file
    try:
        with open(specified_list_path, "r") as file:
            tasker_list = load(file)

    except decoder.JSONDecodeError as error:
        print(f"Problem with {list_type} JSON file: {error}")
        return

    except IOError as error:
        print(f"Couldn't open the {list_type} file: {error}")
        return

    except Exception as Error:
        print(f"Something unexpected went wrong: {error}")
        return

    #Add attribute to JSON file
    tasker_list.append(type_attributes)
    
    #Rewrite JSON file
    try:    
        with open(specified_list_path, "w") as file:
            dump(tasker_list, file, indent=6, skipkeys=True)

            #Explain what happened to user
            if args.verbose:
                print(f"Added to {list_type}  @ {specified_list_path}")

    except decoder.JSONDecodeError as error:
        print(f"Problem with {list_type} JSON file: {error}")
        print("Failed to update list")
        return

    except IOError as error:
        print(f"Couldn't open the {list_type} file: {error}")
        print("Failed to update list")
        return

    except Exception as error:
        print(f"Something unexpected went wrong: {error}")
        print("Failed to update list")
        return


def make_path_for_tasker(tasker_path):
    """Function that makes path of tasker if necessary"""

    #If path doesn't exist then make path
    if not path.exists(tasker_path):

        try:
            makedirs(tasker_path)

        except OSError as error:
            
            print(f"Couldn't make directory for tasker config: {error}")
            return


    #map of tasker config files
    tasker_files = {}
    tasker_files[tasker_config] = sep.join([tasker_path, f"{tasker_config}.json"])
    tasker_files[list_of_notes] = sep.join([tasker_path, f"{list_of_notes}.json"])
    tasker_files[list_of_tasks] = sep.join([tasker_path, f"{list_of_tasks}.json"])

    #Make necessary files
    for file_name, file_path in tasker_files.items():

        print(f"Trying to make following path: {file_path}")

        if path.exists(file_path):
            user_input = input(f"{file_path} already exists would you like to overwrrite it? (y/N): ")

            while user_input not in ["y", "Y", "n", "N"]:
                user_input = input(f"Invalid input please try again (y/N): ")

            if user_input.lower() == "n":
                print(f"Aborted trying to make {file_path} directory\n")
                continue

        try:
            with open(file_path, "w") as file:
                
                if file_name == tasker_config:
                    dump(tasker_files, file, indent=6)

                else:
                    dump([], file, indent=6)
                    
            
            print(f"Successfully made {file_name}\n")

        except IOError as error:
            print(f"Couldn't open {file_path} because of {error}")

        except Exception as error:
            print(f"Something went wrong: {error}")

def make_default_tasker_path():
    """Function makes default tasker path"""
    make_path_for_tasker(get_tasker_path())

def get_tasker_path(expanded_path=True):
    """Function that returns default tasker path"""

    DEFAULT_PATH = sep.join(["~", ".config", "tasker"])
    EXPANDED_DEFAULT_PATH = path.expanduser(DEFAULT_PATH)

    return EXPANDED_DEFAULT_PATH if expanded_path else DEFAULT_PATH

def get_tasker_config_file_paths():
    """Function that gets tasker config file that has all of the paths to other tasker files"""

    PATH_TO_TASKER = get_tasker_path()

    TASKER_CONFIG_PATH = sep.join([PATH_TO_TASKER, f"{tasker_config}.json"])

    #If path note made create tasker files if specified
    if not path.exists(PATH_TO_TASKER):

        user_input = input(f"{PATH_TO_TASKER} doesn't exist would you like to recreate it and all tasker config files?  (y/N): ")

        while user_input not in ["y", "Y", "n", "N"]:
            user_input = input(f"Invalid input please try again (y/N): ")

        if user_input.lower() == "n":
            print(f"Aborted trying to make {PATH_TO_TASKER} directory\n")
            return

        make_default_tasker_path()

    try:
        with open(TASKER_CONFIG_PATH, "r") as file:
            tasker_file_paths = load(file)

    except decoder.JSONDecodeError as error:
        print(f"Couldn't open config JSON file: {error}")
        return

    except IOError as error:
        print(f"Couldn't open file: {error}")
        return

    except Exception as error:
        print(f"Something unexpected happened: {error}")
        return

    return tasker_file_paths

def restore_tasker_file(args, file_path):
    """Restore tasker files if necessary"""

    try:
        with open(file_path, "w") as file:
            dump([], file, indent=6)

            if args.verbose:
                print(f"Successfully restored {file_path}")
    
    except IOError as error:
        print(f"Couldn't create {file_path}: {error}")
        return

    except OSError as error:
        print(f"OS didn't allow for tasker to create {file_path}: {error}")
        return

    except Exception as error:
        print(f"Something unexpected happened: {error}")
        return

    return file_path

    
       

                 
