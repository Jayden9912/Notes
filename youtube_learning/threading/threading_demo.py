# learning from https://www.youtube.com/watch?v=IEEhzQoKtQU&ab_channel=CoreySchafer
import threading
import time
import concurrent.futures

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print("Done sleeping...")


"""
first example: using threading
"""
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

"""
second example: running 10 times using for loop
"""
# threads = []
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

"""
third example: using concurrent
"""
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    """
    3.1: return the result in the order of finishing
    """
    # results = [executor.submit(do_something, sec) for sec in secs]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    """
    3.2 return the result in the order of beginning
    """
    results = executor.map(do_something, secs)

finish = time.perf_counter()

print(f"Finished in {round(finish - start,2)} seconds.")
