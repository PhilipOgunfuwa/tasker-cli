from datetime import date
from argparse import ArgumentParser

def create_note():
    pass
def create_task():
    pass


def main():
    
    #Main parser
    main_parser = ArgumentParser(prog="Tasker",
                            description="Task organization and Agenda",
                            epilog="test...")


    #sub parsers
    main_subparser = main_parser.add_subparsers(title="<Title for main subparser>",
                                      description="<Description for main subparser>",
                                      prog="<Prog for main subparser>")

    
    #create command
    create = main_subparser.add_parser("create",
                                  description="<Description for create subparser>",
                                  prog="<Prog name here for create parser>")

    #add help to these (flags for create commmand)
    create.add_argument("-n", "--name", action="store", dest="name", default=None, 
                        metavar="", help="Add name to file")
    create.add_argument("-da", "--dateassigned", action="store", dest="date_assigned",
                        metavar="", default=date.today(), help="Date when task is assigned") 
    create.add_argument("-dd", "--duedate", action="store", dest="due_date", metavar="",
                        default=date.today())
    create.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=True,
                        help="Verbosely explain what happened")
    create.add_argument("-q", "--quiet", action="store_false", dest="verbose",
                        help="Dont explain what happened")


    create_subparser = create.add_subparsers(title="<Title for create subparser>",
                                             description="<Sub commmands for creating notes, tasks, group tasks, etc>",
                                             prog="<Sub commands for creating notes, tasks, group tasks, etc>")


    #possible commands for create
    note = create_subparser.add_parser("note",
                                       description="<Implement Later>",
                                       prog="<Implement Even Later>")

    
    note.set_defaults(func=create_note)

    main_parser.parse_args()

if __name__ == "__main__":
    main()
