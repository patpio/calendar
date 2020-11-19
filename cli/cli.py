from cli.cmds.no_command import NoCommand


class Cli:
    def __init__(self, cmds):
        self.cmds = cmds

    def get_commands(self):
        return {cls.name: cls for cls in self.cmds}

    def parse_command(self, cmd):
        cmds = self.get_commands()
        command = cmds.setdefault(cmd, NoCommand)
        return command(cmd)

    def get_user_command(self):
        cmds = {}
        for idx, cmd in enumerate(self.get_commands()):
            cmds[str(idx + 1)] = cmd
            print(f'{idx + 1}. {cmd}')

        user_command = input('Choose command\n')
        command = self.parse_command(cmds.setdefault(user_command, user_command))
        command.execute()

    def run(self):
        while True:
            self.get_user_command()
