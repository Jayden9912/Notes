# learning from https://www.youtube.com/watch?v=fKl2JW_qrso&ab_channel=CoreySchafer
import multiprocessing
import time
import concurrent.futures


start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping {seconds} second...")
    time.sleep(seconds)
    print("Done sleeping...")
    return f"Done sleeping {seconds} seconds"


"""
first example
"""

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# p1.start()
# p2.start()

# p1.join()
# p2.join()

"""
second example: using for loop
"""
# processes = []
# for _ in range(10):
#     p = multiprocessing.Process(target=do_something)
#     p.start()
#     processes.append(p)

# for process in processes:
#     process.join()


"""
third example: using concurrent
"""

with concurrent.futures.ProcessPoolExecutor() as executor:
    """
    3.1 no loop
    """
    # f1 = executor.submit(do_something, 1.5)
    # print(f1.result())

    """
    3.2 loop using list comprehension (futures obj is returned)
    """
    # results = [executor.submit(do_something, 1.5) for _ in range(10)]

    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    """
    3.3 using map (result is returned)
    """
    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)  # exception will only be raised when result is processed

finish = time.perf_counter()

print(f"Finished in {round(finish - start,2)} seconds.")
