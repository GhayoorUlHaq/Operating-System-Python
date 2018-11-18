processes = []
dictionary = {
    "name": "P1",
    "arrival_time": 1,
    "brust_time": 16
}
processes.append(dictionary)
dictionary = {
    "name": "P2",
    "arrival_time": 6,
    "brust_time": 3
}
processes.append(dictionary)
dictionary = {
    "name": "P3",
    "arrival_time": 5,
    "brust_time": 4
}
processes.append(dictionary)
dictionary = {
    "name": "P4",
    "arrival_time": 9,
    "brust_time": 2
}
processes.append(dictionary)

print "Process\t\tArrival Time\t\tBrust Time"
for p in processes:
    print p['name']+"\t\t\t"+str(p['arrival_time'])+"\t\t\t\t\t"+str(p["brust_time"])
print("------------------------------\n\n")