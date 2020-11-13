from cli.cmds.no_command import NoCommand


class Cli:
    def __init__(self, cmds):
        self.cmds = cmds

    def get_commands(self):
        return {cls.name: cls for cls in self.cmds}

    def parse_command(self, cmd):
        cmds = self.get_commands()
        command = cmds.setdefault(cmd, NoCommand) #Zwraca wartosc po kluczu, jesli nie istnieje to wtedy drugi parametr
        return command(cmd)

    def get_user_command(self):
        for idx, cmd in enumerate(self.get_commands()): # TODO zmienic tak zeby komendy mozna bylo wybierac i numerem i nazwa
            print(f'{idx + 1}. {cmd}')

        user_command = input('Choose command\n')
        command = self.parse_command(user_command)
        command.execute()

    def run(self):
        while True:
            self.get_user_command()
