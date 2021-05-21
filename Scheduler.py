from __future__ import annotations
from typing import *
import Process

class Scheduler :
    now: int
    waitTime: int
    idleCycles: int
    waitQueue: List[Process.ProcessControlBLock]
    runQueue: List[Process.ProcessControlBLock]
    finished: List[Process.ProcessControlBLock]
    utilization: float

    def __init__(self):
        self.now = 0
        self.waitQueue = []
        self.runQueue = []
        self.finished = []
        self.waitTime = 0
        self.idleCycles = 0
        self.utilization = -1

    def _executeAll(self, processes : List[Process.ProcessControlBLock]):
        pass

    def executeAll(self, processes : List[Process.ProcessControlBLock]):
        if self.finished == [] :
            self._executeAll(processes)
        else :
            raise Exception("Scheduler not in initialized state")

    def report(self):
        if self.utilization == -1 :
            print(f"Nothing to report")
        else :
            print(f"waitTime: {self.waitTime}; utilization: {self.utilization}")

class NonPreemptiveFIFOScheduler(Scheduler) :

    def _executeAll(self, processes : List[Process.ProcessControlBLock]):
        while(len(processes) > 0) :
            current = processes.pop(0) #remove the first process
            instr = current.nextInstruction()
            self.now += Process.ProcessControlBLock.BLOCK_DELAY if instr == 2 else 1
            while(instr != -1) :
                #update waitTIme <<<< IMPLEMENT THIS!!!
                self.idleCycles += Process.ProcessControlBLock.BLOCK_DELAY if instr == 2 else 0
                instr = current.nextInstruction()
                self.now += Process.ProcessControlBLock.BLOCK_DELAY if instr == 2 else 1
        self.utilization = (self.now - self.idleCycles) / float(self.now)

class PreemptiveFIFOScheduler(Scheduler) :

    def _executeAll(self, processes: List[Process.ProcessControlBLock]):
        print("IMPLEMENT ME!")

class ShortestJobFirstScheduler(Scheduler) :

    def _executeAll(self, processes : List[Process.ProcessControlBLock]):
        print("IMPLEMENT ME!")
