from multiprocessing import Queue
from threading import Thread, RLock
import time
import random


class Consumer(Thread):
    def __init__(self, queue: Queue, idx: int, glock: RLock):
        super(Consumer, self).__init__()
        self.queue = queue
        self.idx = idx
        self.sleep = lambda: random.random() * 2
        self.lock = glock

    def run(self):
        try:
            while True:
                self.consume()
                time.sleep(self.sleep())
        except KeyboardInterrupt:
            return

    def consume(self):
        if not self.queue.empty():
            item = self.queue.get()
            with self.lock:
                print(f"Consumer({self.idx}): Received item {str(item)}")
        return
