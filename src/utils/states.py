# Import the State and StatesGroup classes from the FSM
from aiogram.fsm.state import State, StatesGroup

# State group called ParentStates
class ParentStates(StatesGroup):
    # Define a single state called 'start'
    start = State()

# Another state group called ChildStates
class ChildStates(StatesGroup):
    # Define a single state called 'task'
    task = State()
