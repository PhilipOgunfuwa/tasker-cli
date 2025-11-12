from task_object import Task
from os import path, sep, getlogin, makedirs
from argparse import ArgumentParser
from create_argument_template import template

    
def create_note(args):
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

            file.write(f"\n* Properties\n")
            file.write("\n:PROPERTIES:")
            file.write(f"\n:CLASS: {args.class_name}")
            file.write(f"\n:TYPE: {args.creation_type}")
            file.write(f"\n:Started: <{args.date_assigned}>")
            file.write(f"\n:DEADLINE: <{args.due_date}>\n")
            file.write(f"* ")

            #Only prints out feedback if user uses -q argument
            if args.verbose:
                print(f"Created org file: {note_name}")
                
    except IOError as error:
        print(f"Error when trying to open file: {error}")



def create_task(args):
    """Function to create a task by adding it to a json file"""

    #Logged in users name
    user_name = getlogin()

    #Os specific delimiter "/" or "\"
    os_delimiter = sep

    #Path for tasker
    tasks_path = os_delimiter.join(["/home", user_name, ".config", "tasker"])

    #json file for task
    json_file = f"{args.file_name}.json" 

    create_file_at_path(tasks_path, json_file)
    
    


    



def create_task_group(args):
    pass

def add_to_task_groups(args):
    pass

def create_file_at_path(given_path, file):

    #Path for file
    path_for_file = f"{given_path}{sep}{file}"

    #Create path if path doesn't exist
    if not path.exists(given_path):

        try:
            makedirs(given_path)

        except OSError as error:
            print(f"Error trying to create task: {error}")
            return
    
    #Dont do anything if file already exists
    if path.isfile(path_for_file):
        print("File already exists")
        return

    #Open file at given path
    try:
        with open(path_for_file, "x") as file:
           pass

    #Error trying to open file
    except IOError as error:
        print(f"Error trying to make file: {error}")

def no_function(args):
    """Empty function for when a command has no immediate functions"""
    pass
    
def main():
    
    #Main parser
    main_parser = ArgumentParser(prog="Tasker",
                            description="Task organization and Agenda")


    #sub parsers
    main_subparser = main_parser.add_subparsers(title="<Title for main subparser>",
                                      description="<Description for main subparser>",
                                      prog="<Prog for main subparser>")

    
    #Parser for create command
    create = main_subparser.add_parser("create",
                                  description="<Description for create subparser>",
                                  prog="<Prog name here for create parser>")

    create_subparser = create.add_subparsers(title="<Title for create subparser>",
                                             description="<Sub commmands for creating notes, tasks, group tasks, etc>",
                                             prog="<Sub commands for creating notes, tasks, group tasks, etc>")


    #Parser for note command 
    note = create_subparser.add_parser("note",
                                       parents=[template],
                                       description="<Implement Later>",
                                       prog="<Implement Even Later>",
                                       add_help=False)

    #Parser for task command
    task = create_subparser.add_parser("task",
                                       parents=[template],
                                       description="<Implement Later>",
                                       prog="<Implemenet Even Later>",
                                       add_help=False)

    #Giving attribute of func to hold function to run when command is called
    main_parser.set_defaults(func=no_function)
    note.set_defaults(func=create_note)
    task.set_defaults(func=create_task)

    args = main_parser.parse_args()
    
    
    args.func(args)

if __name__ == "__main__":
    main()

