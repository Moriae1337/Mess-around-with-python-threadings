import concurrent.futures
import queue
import time

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def worker(task_queue, result_queue):
    while not task_queue.empty():
        try:
            n = task_queue.get_nowait()
            steps = collatz_steps(n)
            result_queue.put(steps)
        except queue.Empty:
            break

def main():
    N = 10_000_000
    num_threads = 8
    task_queue = queue.Queue()
    result_queue = queue.Queue()

    for i in range(1, N + 1):
        task_queue.put(i)

    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(worker, task_queue, result_queue) for _ in range(num_threads)]

        concurrent.futures.wait(futures)

    total_steps = 0
    processed = 0
    while not result_queue.empty():
        total_steps += result_queue.get()
        processed += 1

    average_steps = total_steps / processed
    end_time = time.time()

    print(f"Середня кількість кроків: {average_steps:.2f}")
    print(f"Час виконання: {end_time - start_time:.2f} секунд")

if __name__ == "__main__":
    main()
