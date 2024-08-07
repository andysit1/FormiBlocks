from queue import Queue
from src.components.models import CommandBlockState

"""
  Queue command blocks and run them on os
"""


class CommandExecutioner:
  def __init__(self) -> None:
    self.event_queue : Queue[CommandBlockState] = Queue()

  def add_events(self, commands : list):
    for command in commands:
      if isinstance(command, CommandBlockState):
        self.add_event(command=command)

  def add_event(self, command : CommandBlockState):
    self.event_queue.put(command)

  def run(self):
    #triggers all event command blocks until empty
    while self.event_queue.qsize > 0:
      event = self.event_queue.get()
      event.run()

