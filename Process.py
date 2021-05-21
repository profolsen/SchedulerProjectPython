from __future__ import annotations
from typing import *


# requires Python version 3.8+
class ProcessControlBLock:
    # class variables
    NEW = 0
    READY = 1
    RUNNING = 2
    WAITING = 3
    TERMINATED = 4
    # generating new IDs.
    ID_SOURCE = 0
    #the amount of time process blocks for I/O:
    BLOCK_DELAY = 5

    # instance variables
    id: int
    state: int
    pc: int
    priority: int
    # for the instructions list:
    # -1 = HALT
    # 1 = some computation
    # 2 = I/O (block and wait).  This instruction always blocks for precisely BLOCK_DELAY cycles.
    instructions: List[int]

    def __init__(self, instructions: List[int] = [-1], priority: int = 50):
        if priority > 99 or priority < 0 :
            raise Exception(f"priority of process outside legal range {priority}")
        if instructions[-1] != -1 :
            raise Exception(f"Program does not end with halt: {instructions}")
        self.state = ProcessControlBLock.NEW
        ProcessControlBLock.ID_SOURCE += 1
        self.id = ProcessControlBLock.ID_SOURCE
        self.instructions = instructions
        self.pc = 0
        self.priority = priority

    def __str__(self):
        return f"<{self.id}, {self.stateAsString}>";

    def nextInstruction(self):
        self.pc += 1
        return self.instructions[self.pc - 1]

    def fork(self):
        if self.state != ProcessControlBLock.NEW :
            raise Exception("Process must be NEW to be forked on this system.")
        else :
            return ProcessControlBLock(self.instructions, self.priority)

    @property
    def stateAsString(self):
        if self.state == ProcessControlBLock.NEW:
            return "NEW"
        elif self.state == ProcessControlBLock.READY:
            return "READY"
        elif self.state == ProcessControlBLock.RUNNING:
            return "RUNNING"
        elif self.state == ProcessControlBLock.WAITING:
            return "WAITING"
        elif self.state == ProcessControlBLock.TERMINATED:
            return "TERMINATED"
        else:
            return f"INVALID{self.state}"
