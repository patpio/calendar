from cli.cmds.abs_command import AbsCommand


class ShowEvents(AbsCommand):
    name = 'Show Events'

    def execute(self):
        for event in self.events.get_events():
            print(event)
