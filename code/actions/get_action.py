from enum import Enum
from actions import *

class Get_Action(Enum):
    MOVE = Move
    BASH_ATTACK = Bash_Attack
    SPINNING_ATTACK = Spinning_Attack