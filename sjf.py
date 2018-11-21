processes = []
with open("file.txt", 'r') as lines:
    for line in lines:
        process_name, arrival_time, brust_time = line.split(" ")
        dictionary = {}
        dictionary['name'] = process_name.strip()
        dictionary['arrival_time'] = int(arrival_time.strip())
        dictionary['brust_time'] = int(brust_time.strip())

        processes.append(dictionary)
#sorting according to brust time
processes.sort(key = lambda process: process['brust_time'])
#calculating waiting time turnaroud of each process
waiting_time = 0
for process in processes:
    process['waiting_time'] = waiting_time
    process['turnaround_time'] = process['brust_time'] + waiting_time
    waiting_time = waiting_time + process['brust_time']



gantt_chart = '0'
total_waiting_time = 0
total_turnaround_time = 0
print("Process" + "\t\tArrival" + "\t\tBurst " + "\t\tWaiting" + "\t\tTurnaround Time")
#going through processes
for process in processes:
    gantt_chart += "____"+str(process['turnaround_time'])+"|"+str(process['name'])
    total_turnaround_time += process['turnaround_time']
    total_waiting_time += process['waiting_time']
    print(process['name'] + "\t\t\t"+str(process['arrival_time']) + "\t\t\t"+str(process['brust_time']) + "\t\t\t"+str(process['waiting_time']) + "\t\t\t"+str(process['turnaround_time']))
#print gantt chart
print "\nGantt Chart:\t",
print gantt_chart
#total turnaround and waiting time
print("\nAverage Waiting time: "+ str(total_waiting_time/len(processes)))
print("Average Turnaround time: "+ str(total_turnaround_time/len(processes)))