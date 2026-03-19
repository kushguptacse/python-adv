from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(lambda x: x**2, i) for i in range(1, 11)]

    for future in as_completed(futures):
        print(future.result())