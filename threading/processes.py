from multiprocessing import Process
import time

def worker():
    print("Start worker")
    time.sleep(2)
    print("End worker")

p1 = Process(target=worker)

print(f"Alive: {p1.is_alive()}")  # False

p1.start()
print(f"Alive: {p1.is_alive()}")  # True

p1.join()