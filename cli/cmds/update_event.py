from cli.cmds.abs_command import AbsCommand


class UpdateEvent(AbsCommand):
    name = 'Update Event'

    def execute(self):
        user_idx = input('Provide event index\n')

        try:
            idx = int(user_idx)
        except ValueError:
            print('Index must be a number')
        else:
            while True:
                config_key = input('Provide update key\n')
                if not config_key:
                    break
                config_value = input('Provide update value\n')
                config = {config_key: config_value}
                try:
                    self.events.update_event(idx, config)
                except ValueError:
                    print("Meeting duration under 5 minutes doesn't make sense.")
