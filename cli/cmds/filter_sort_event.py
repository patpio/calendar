from re import findall

from cli.cmds.abs_command import AbsCommand
from helpers.helpers import parse_user_filter


class FilterSortEvent(AbsCommand):
    name = 'Filter Sort Event'

    def execute(self):
        while True:
            filter_key = input('Provide filter key (omit if only sorting desired)\n')
            if not filter_key:
                break
            filter_value_min = parse_user_filter(filter_key, input('Provide min value\n'))
            filter_value_max = parse_user_filter(filter_key, input('Provide max value\n'))

            AbsCommand.events.filter_config[filter_key] = {'min': filter_value_min, 'max': filter_value_max} # self -> Abscommand

        sort_keys = input('Provide sort keys (omit if not desired)\n')
        AbsCommand.events.sort_config = findall(r'\w+', sort_keys)

        try:
            for event in self.events.get_events():
                print(event)
        except AttributeError:
            print('Wrong key')

        AbsCommand.events.filter_config = {}
        AbsCommand.events.sort_config = {}
