# CSC 432 Project 2 -- Scheduling
# You have three tasks:
# (1) Implement updating of wait time in non-preemptive fifo scheduler (Scheduler.py)
# (2) Implement preemptive fifo scheduler (including stat calcuation) (Scheduler.py)
# (3) Implement shortest job first scheduler (including stat calculation) (Scheduler.py)
import Process
import Scheduler

if __name__ == '__main__':
    arch_1 = Process.ProcessControlBLock([1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, -1])
    arch_2 = Process.ProcessControlBLock([1, 1, 2, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, -1])
    arch_3 = Process.ProcessControlBLock([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, -1])

    nonpreemptive_fifo_processes = [arch_1.fork(), arch_2.fork(), arch_3.fork()]
    preemptive_fifo_processes = [arch_1.fork(), arch_2.fork(), arch_3.fork()]
    shortest_job_first_processes = [arch_1.fork(), arch_2.fork(), arch_3.fork()]

    nonpreemptive_fifo_scheduler = Scheduler.NonPreemptiveFIFOScheduler()
    preemptive_fifo_scheduler = Scheduler.PreemptiveFIFOScheduler()
    shortest_job_first_scheduler = Scheduler.ShortestJobFirstScheduler()

    nonpreemptive_fifo_scheduler.executeAll(nonpreemptive_fifo_processes)
    nonpreemptive_fifo_scheduler.report()

    preemptive_fifo_scheduler.executeAll(preemptive_fifo_processes)
    preemptive_fifo_scheduler.report()

    shortest_job_first_scheduler.executeAll(shortest_job_first_processes)
    shortest_job_first_scheduler.report()
