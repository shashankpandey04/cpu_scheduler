def fcfs(processes):
    procs = sorted(processes, key=lambda x: x['arrival'])
    time = 0
    result = []
    for p in procs:
        start = max(time, p['arrival'])
        completion = start + p['burst']
        turnaround = completion - p['arrival']
        waiting = turnaround - p['burst']
        result.append({
            'pid': p['pid'],
            'arrival': p['arrival'],
            'burst': p['burst'],
            'start': start,
            'completion': completion,
            'waiting': waiting,
            'turnaround': turnaround
        })
        time = completion
    return result
