from cli.cmds.abs_command import AbsCommand


class DeleteEvent(AbsCommand):
    name = 'Delete Event'

    def execute(self):
        idx = input(f'Provide event index:\n')

        if idx.isdigit():
            self.events.delete_event(int(idx))
        else:
            print('Index must be a number')
