from cli.cmds.abs_command import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, name):
        self.name = name

    def execute(self):
        print(f'Incorrect command: {self.name}')
