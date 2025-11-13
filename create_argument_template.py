from argparse import ArgumentParser
from datetime import date

def make_templates():
    #Template parser that simply has arguments I want as a template

    create_template = ArgumentParser(prog="Template",
                                     description="Template Description")

    create_template.add_argument("-n", "--name", action="store", dest="file_name", default=None, 
                                 required=True, metavar="", help="Add name to file")

    create_template.add_argument("-d", "--description", action="store", dest="description", default=None,
                                 metavar="", help="Give description to task or note")

    create_template.add_argument("-da", "--dateassigned", action="store", dest="date_assigned",
                                 metavar="", default=date.today(), help="Date when task is assigned") 

    create_template.add_argument("-dd", "--duedate", action="store", dest="due_date", metavar="",
                                 default=date.today(), help="Date when task is due")

    create_template.add_argument("-c", "--class", action="store", dest="class_name", metavar="",
                                 help="Class that the note or task is for")

    create_template.add_argument("-t", "--type", action="store", dest="creation_type", metavar="",
                                 choices=["Lecture", "Assignment", "General", "Project"], default="General",
                                 help="The type of note or task: Lecture, Assignment, General, Project")

    create_template.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=True,
                                 help="Verbosely explain what happened")

    create_template.add_argument("-q", "--quiet", action="store_false", dest="verbose",
                                 help="Don't explain what happened")

    show_template = ArgumentParser(prog="Template",
                                   description="Template Description")

    show_template.add_argument("-n", "--name", action="store", dest="file_name", metavar="",
                               help="File name for task, group task, or note to find")

    show_template.add_argument("-v", "--verbose", action="store_true", dest="verbose",
                               help="Verbosely explain what happened")

    show_template.add_argument("-q", "--quiet", action="store_false", dest="verbose",
                               help="Don't explain what happened")

    remove_template = ArgumentParser(prog="Template",
                                     description="Template Description")

    remove_template.add_argument("-n", "--name", action="store", required=True, metavar="", nargs="*",
                                 dest="file_names", help="Name(s) of file(s) to be removed")

    remove_template.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=True,
                                 help="Verbosely explain what happened")

    remove_template.add_argument("-q", "--quiet", action="store_false", dest="verbose",
                                 help="Don't explain what happened")

    return create_template, show_template, remove_template

if __name__ == "__main__":
   make_templates()
