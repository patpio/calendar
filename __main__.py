from cli.cli import Cli
from cli.cmds.create_event import CreateEvent
from cli.cmds.show_events import ShowEvents
from events import Events

cmds = (CreateEvent, ShowEvents)
cli = Cli(cmds)

cli.run()