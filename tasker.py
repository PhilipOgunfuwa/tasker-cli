#!/usr/bin/python3

from datetime import date
from json import dump, load, decoder 
from os import path, sep, getlogin, makedirs
from argparse import ArgumentParser
from create_argument_template import make_templates
from create_command import create_note_function, create_task_function
from show_command import show_note_function, show_task_function
from remove_command import remove_note_function, remove_task_function

#Argument templates for create, show, and remove commands
create_template, show_template, remove_template = make_templates()


def no_function(args):
    """Empty function for when a command has no immediate functions"""
    pass
    
def main():
    
    #Main parser
    main_parser = ArgumentParser(prog="Tasker",
                                 description="Task and Note manager",
                                 usage="%(prog)s [options] or %(prog)s [argument]")

    #sub parsers
    main_subparser = main_parser.add_subparsers()

    
    #Parser for create command
    create = main_subparser.add_parser("create", prog="create",
                                       description="Create a org mode note or task",
                                       usage="%(prog)s [options] or %(prog)s [argument]")

    #Subparser that searches for note and task after create is read
    create_subparser = create.add_subparsers()


    #Parser for note command 
    create_note = create_subparser.add_parser("note",
                                              parents=[create_template],
                                              description="Create an org mode note",
                                              prog="note",
                                              usage="%(prog)s -n 'file name' [other options]",
                                              add_help=False)

    #Parser for task command
    create_task = create_subparser.add_parser("task",
                                              parents=[create_template],
                                              description="Create a task",
                                              prog="task",
                                              usage="%(prog)s -n 'file name' [other options]",
                                              add_help=False)
    
    
    #Parser for show command
    show = main_subparser.add_parser("show",
                                     description="Show all or specified note(s) or task(s)",
                                     prog="show",
                                     usage="%(prog)s [option] or %(prog)s [argument]")

    show_subparser = show.add_subparsers()

    show_note = show_subparser.add_parser("note",
                                          parents=[show_template],
                                          description="Show org mode note(s)",
                                          prog="note",
                                          usage="%(prog)s -n 'file name1' 'file name 2' [other options]",
                                          add_help=False)

    show_task = show_subparser.add_parser("task",
                                          parents=[show_template],
                                          description="Show task(s)",
                                          prog="task",
                                          usage="%(progs)s -n 'fil name1' 'file name 2' [other options]",
                                          add_help=False)

    #Parser for remove command
    remove = main_subparser.add_parser("remove",
                                       description="Delete specified note(s) or task(s)",
                                       prog="remove",
                                       usage="%(prog)s [option] or %(prog)s [argument]")

    remove_subparser = remove.add_subparsers()

    remove_note = remove_subparser.add_parser("note",
                                              parents=[remove_template],
                                              description="Remove org mode note(s) from list of notes",
                                              prog="note",
                                              usage="%(prog)s -n 'file name1' 'file name2' [other options]",
                                              add_help=False)

    remove_task = remove_subparser.add_parser("task",
                                              parents=[remove_template],
                                              description="Remove task(s) from list of notes",
                                              prog="task",
                                              usage="%(prog)s -n 'file name1' 'file name2' [other options]",
                                              add_help=False)

    

    #Giving attribute of func to hold function to run when command is called
    main_parser.set_defaults(func=no_function)
    create_note.set_defaults(func=create_note_function)
    create_task.set_defaults(func=create_task_function)
    show_note.set_defaults(func=show_note_function)
    show_task.set_defaults(func=show_task_function)
    remove_note.set_defaults(func=remove_note_function)
    remove_task.set_defaults(func=remove_task_function)
    

    #Main parser reads commands when tasker is called  
    args = main_parser.parse_args()
    
    #Appropriate functions are called based off of args 
    args.func(args)

if __name__ == "__main__":
    main()

