import multiprocessing

def worker(num):
    """A simple worker function that prints its process ID and the input number."""
    print(f"Worker {multiprocessing.current_process().pid} processing {num}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    processes = []

    for num in numbers:
        p = multiprocessing.Process(target=worker, args=(num,))
        processes.append(p)

    for p in processes:
        p.start()

    for p in processes:
        p.join()