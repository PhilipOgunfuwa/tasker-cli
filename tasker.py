from datetime import date
from json import dump, load, decoder 
from os import path, sep, getlogin, makedirs
from argparse import ArgumentParser
from create_argument_template import make_templates
from create_command import create_note_function, create_task_function, create_task_group_function
from update_tasker_files import add_note_to_list, create_file_at_tasker
from remove_command import remove_task_function, remove_note_function

create_template, show_template, remove_template = make_templates()

def add_to_task_groups(args):
    pass

def show_note_function(args):
    pass

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
    create_note = create_subparser.add_parser("note",
                                       parents=[create_template],
                                       description="<Implement Later>",
                                       prog="<Implement Even Later>",
                                       add_help=False)

    #Parser for task command
    create_task = create_subparser.add_parser("task",
                                       parents=[create_template],
                                       description="<Implement Later>",
                                       prog="<Implemenet Even Later>",
                                       add_help=False)
    
    #FIXME NOT IMPLEMENTED
    #Parser for task group command
    create_task_group = create_subparser.add_parser("task group", 
                                             parents=[create_template],
                                             description="<Implement Later>",
                                             prog="<Implement Even Later>",
                                             add_help=False)

    
    
    #Parser for show command
    show = main_subparser.add_parser("show",
                                     description="<Description for show subparser>",
                                     prog="<Prog nme for show>")

    show_subparser = show.add_subparsers(title="<Title for create subparser>",
                                         description="<Sub commands for showing notes, tasks, tasks groups>",
                                         prog="<Sub commands for showing notes, tasks, tasks groups>")

    show_note = show_subparser.add_parser("note",
                                          parents=[show_template],
                                          description="<Implement Later>",
                                          prog="<Implement Even Later>",
                                          add_help=False)

    show_task = show_subparser.add_parser("show",
                                          parents=[show_template],
                                          description="<Implement Later>",
                                          prog="<Implement Even Later>",
                                          add_help=False)

    #Parser for remove command
    remove = main_subparser.add_parser("remove",
                                       description="<Description for remove subparser>",
                                       prog="<Prog name for remove>")

    remove_subparser = remove.add_subparsers(title="<Title for remove subparser>",
                                            description="<Sub commands for removing, notes, tasks, task groups>",
                                            prog="<Sub commands for removing notes, tasks, task groups>")

    remove_note = remove_subparser.add_parser("note",
                                              parents=[remove_template],
                                              description="<Implement Later>",
                                              prog="<Implement Even Later>",
                                              add_help=False)

    remove_task = remove_subparser.add_parser("task",
                                              parents=[remove_template],
                                              description="<Implement Later>",
                                              prog="<Implement Even Later>",
                                              add_help=False)

    

    #Giving attribute of func to hold function to run when command is called
    main_parser.set_defaults(func=no_function)
    create_note.set_defaults(func=create_note_function)
    create_task.set_defaults(func=create_task_function)
    create_task_group.set_defaults(func=create_task_group)
    show_note.set_defaults(func=show_note_function)
    remove_task.set_defaults(func=remove_task_function)
    remove_note.set_defaults(func=remove_note_function)
    

    
    args = main_parser.parse_args()
    
    
    args.func(args)

if __name__ == "__main__":
    main()

