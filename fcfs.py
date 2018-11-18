import time

from queue import Queue
from processes import processes


#sorting according to arrival time
processes.sort(key=lambda process: process['arrival_time'])

#loading ready queue
ready_queue = Queue()
ready_queue.print_queue()

finist_time = []
chart = ""
current_time = 0
for process in processes:
    if process['arrival_time'] == current_time:
        ready_queue.enqueue(process)

    if not ready_queue.is_empty():
        current_process = ready_queue.dequeue()
        if(current_process['arrival_time'] == current_time):
            chart += "__%d"%current_process["arrival_time"]
            time.sleep(current_process["brust_time"])
            current_time = current_process["brust_time"]
            print current_time, current_process['brust_time']
        else:
            ready_queue.enqueue(current_process)


    #check queue
    pass
    #process

print chart
#
#
