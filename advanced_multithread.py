import concurrent.futures
import time
import timeit

from threading import Semaphore

my_semaphore = Semaphore(2)


def do_it(tid):
    # semaphore ensure the atomic operation
    my_semaphore.acquire()
    result = ""
    # time.sleep(1)
    result += f"task {tid} step1\n"
    pass
    # time.sleep(1)
    result += f"task {tid} step2\n"
    pass
    # time.sleep(1)
    result += f"task {tid} step3\n"
    pass
    # time.sleep(1)
    result += f"task {tid} completed.\n"

    # atomic operation
    print(result, end="")

    my_semaphore.release()
    return 0


start_time = timeit.default_timer()

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
    future_to_tid = {executor.submit(do_it, tid): tid for tid in range(100)}
    for future in concurrent.futures.as_completed(future_to_tid):
        tid = future_to_tid[future]
        try:
            data = future.result()
        except Exception as e:
            print('%r generated an exception: %s\n' % (tid, e), end="")
        else:
            print('task %r returns %d\n' % (tid, data), end="")

end_time = timeit.default_timer()
print(f'time = {end_time - start_time}s')
