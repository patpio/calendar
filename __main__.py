from cli import Cli
from cli.cmds.create_event import CreateEvent
from cli.cmds.delete_event import DeleteEvent
from cli.cmds.filter_sort_event import FilterSortEvent
from cli.cmds.show_events import ShowEvents
from cli.cmds.update_event import UpdateEvent

cmds = (CreateEvent, ShowEvents, DeleteEvent, UpdateEvent, FilterSortEvent)
cli = Cli(cmds)

cli.run()
