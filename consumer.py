from multiprocessing import Queue, Process
import time


class Consumer(Process):
    def __init__(self, queue: Queue, idx: int):
        super(Consumer, self)
        self.queue = queue
        self.idx = idx

    def run(self):
        while True:
            self.consume()

    def consume(self):
        if not self.queue.empty():
            item = self.queue.get()
            print(f"Consumer({self.idx}): Received item {str(item)}")
            time.sleep(2)
        return
