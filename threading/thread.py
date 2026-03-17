from threading import Thread
import time

def worker(sleep_time: float) -> None:
    print("Start worker")
    time.sleep(sleep_time)
    print("End worker")

t1 = Thread(name="t1", target=worker, args=(2.0,))

print(f"Ident: {t1.ident}")  # Ident: None
print(f"Alive: {t1.is_alive()}")  # Alive: False
print(f"Name: {t1.name}")  # Name: t1

t1.start() # start the thread
print(f"Ident: {t1.ident}")  # Ident: 126540744336960
print(f"Alive: {t1.is_alive()}")  # Alive: True
print(f"Name: {t1.name}")  # Name: t1

t1.join() # wait for main thread to wait t1 to get completed.
