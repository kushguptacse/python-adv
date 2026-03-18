from concurrent.futures import ProcessPoolExecutor, as_completed

def square(x):
    return x ** 2

with ProcessPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(square, i) for i in range(1, 11)]

    for future in as_completed(futures):
        print(future.result())