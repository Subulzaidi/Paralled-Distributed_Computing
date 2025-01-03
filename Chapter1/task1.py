import time
import multiprocessing
import threading

# Placeholder for the do_something function
def do_something(size, out_list):
    """
    Perform a computational task to simulate workload.
    Appends square of numbers to out_list.
    """
    for i in range(size):
        out_list.append(i * i)

if __name__ == "__main__":
    size = 100000
    procs = 10
    jobs = []

    # Multiprocessing
    start_time = time.time()
    out_list = multiprocessing.Manager().list([[] for _ in range(procs)])

    for i in range(procs):
        process = multiprocessing.Process(target=do_something, args=(size, out_list[i]))
        jobs.append(process)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete (multiprocessing).")
    end_time = time.time()
    print("Multiprocessing time =", end_time - start_time)

    # Reset jobs list for threading
    jobs = []
    threads = 10
    start_time = time.time()
    out_list = [[] for _ in range(threads)]

    for i in range(threads):
        thread = threading.Thread(target=do_something, args=(size, out_list[i]))
        jobs.append(thread)

    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print("List processing complete (multithreading).")
    end_time = time.time()
    print("Multithreading time =", end_time - start_time)
