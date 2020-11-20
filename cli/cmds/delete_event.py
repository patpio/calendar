from cli.cmds.abs_command import AbsCommand


class DeleteEvent(AbsCommand):
    name = 'Delete Event'

    def execute(self):
        user_idx = input(f'Provide event index:\n')

        try:
            idx = int(user_idx)
        except ValueError:
            print('Index must be a number')
        else:
            self.events.delete_event(int(idx))

        # if idx.isdigit():
        #     self.events.delete_event(int(idx))
        # else:
        #     print('Index must be a number')
