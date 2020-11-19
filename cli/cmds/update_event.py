from cli.cmds.abs_command import AbsCommand
from helpers.helpers import parse_user_update


class UpdateEvent(AbsCommand):
    name = 'Update Event'

    def execute(self):
        user_idx = input('Provide event index\n')

        try:
            idx = int(user_idx)
        except ValueError:
            print('Index must be a number')
        else:
            config_key = input('Provide update key\n')
            config_value = parse_user_update(config_key, input('Provide update value\n'))
            config = {config_key: config_value}
            self.events.update_event(idx, config)
