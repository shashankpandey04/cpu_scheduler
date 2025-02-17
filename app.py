from algorithms import fcfs, sjf, round_robin, priority
from visualization import display_results

def get_user_input():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        print(f"Process {i+1}:")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        priority_val = int(input("Priority (lower number = higher priority): "))
        processes.append({
            'pid': i+1,
            'arrival': arrival,
            'burst': burst,
            'priority': priority_val
        })
    time_quantum = int(input("Enter Time Quantum (for RR): "))
    return processes, time_quantum

def main():
    print("CPU Scheduler Simulator")
    processes, tq = get_user_input()
    print("\nChoose Algorithm:\n1. FCFS\n2. SJF\n3. Round Robin\n4. Priority\n5. All")
    choice = int(input("Enter choice: "))

    results = {}

    if choice == 1 or choice == 5:
        res = fcfs.fcfs(processes)
        results["FCFS"] = res
    if choice == 2 or choice == 5:
        res = sjf.sjf(processes)
        results["SJF"] = res
    if choice == 3 or choice == 5:
        res = round_robin.rr(processes, tq)
        results["Round Robin"] = res
    if choice == 4 or choice == 5:
        res = priority.priority(processes)
        results["Priority"] = res

    display_results(results)

if __name__ == "__main__":
    main()
