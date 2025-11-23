Created a simple terminal note and task manager that lets you keep track of tasks and notes you've created.

To be fair this is more for me than anyone else but I think anyone could use it.

* Learned
  * Argparse, os, json, and a little datetime modules
  * Did this entire project without any tutorials and just official
    python documentation
  * Tried to adhere to good coding fundamentals like DRY and got some
    extra practice doing IO with files in python

* Future plans
  * Make it so you can show tasks/notes based off of conditions
  * Have a more centralized config.py file that has more important
    and redundant funcitons in their
  * Add more functionality that would be helpful for my classes
 
* Basic how to use
  * (Recommended to make a bash/powershell alias the script)
  * alias tasker='python3 ~/todo\ cli/tasker.py' (bash on linux)
  * tasker create (note/task) to make org mode note or task
  * tasker show (note/task) to show org mode notes and tasks made by tasker
  * tasker remove (note/task) to remove org mode notes and tasks made by tasker
  * use -h at the end of the commands to get all the necessary options
