from argparse import ArgumentParser
from datetime import date

#Template parser that simply has arguments I want as a template

template = ArgumentParser(prog="Template",
                          description="Template Description")

template.add_argument("-n", "--name", action="store", dest="file_name", default=None, 
                      required=True, metavar="", help="Add name to file")

template.add_argument("-da", "--dateassigned", action="store", dest="date_assigned",
                      metavar="", default=date.today(), help="Date when task is assigned") 

template.add_argument("-dd", "--duedate", action="store", dest="due_date", metavar="",
                      default=date.today(),
                      help="Date when task is due")

template.add_argument("-c", "--class", action="store", dest="class_name", metavar="",
                      help="Class that the note or task is for")

template.add_argument("-t", "--type", action="store", dest="creation_type", metavar="",
                      choices=["Lecture", "Assignment", "General", "Project"], default="General",
                      help="The type of note or task: Lecture, Assignment, General, Project")

template.add_argument("-v", "--verbose", action="store_true", dest="verbose", default=True,
                      help="Verbosely explain what happened")

template.add_argument("-q", "--quiet", action="store_false", dest="verbose",
                      help="Dont explain what happened")

