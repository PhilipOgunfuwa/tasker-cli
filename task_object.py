class Task:
    """Class that will have a task and all its arguments"""

    def __init__(self, args):
        for variable_name, content in vars(args).items():
            setattr(self, variable_name, content)
            
    def print_dir(self):
        print(dir(self))

def main():
    pass

if __name__ == "__main__":
    main()

