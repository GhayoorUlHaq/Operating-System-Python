quantum_time = 3
processes = []
with open("file_rr.txt", 'r') as lines:
    for line in lines:
        process_name, arrival_time, brust_time = line.split(" ")
        dictionary = {}
        dictionary['name'] = process_name.strip()
        dictionary['arrival_time'] = int(arrival_time.strip())
        dictionary['brust_time'] = int(brust_time.strip())
        dictionary['quantum_time'] = quantum_time
        processes.append(dictionary)

print("Process" + "\t\tArrival" + "\t\tBurst " + "\t\tQuantum")
for process in processes:
    print(str(process['name']) + "\t\t\t"+str(process['arrival_time']) + "\t\t\t"+str(process['brust_time']) + "\t\t\t"+str(process['quantum_time']))



gantt_chart = '0'
time_line = 0
#going through processes
for process in processes:
    if process['brust_time'] <= process['quantum_time']:
        time_line += process['brust_time']
        gantt_chart += '___'+str(time_line)+'|'+process['name']
        processes.remove(process)
    elif process['brust_time'] > process['quantum_time']:
        process['brust_time'] = process['brust_time'] - process['quantum_time']
        time_line += process['quantum_time']
        gantt_chart += '___'+str(time_line)+'|'+process['name']
        tem_process = process
        processes.remove(process)
        processes.append(tem_process)

print gantt_chart