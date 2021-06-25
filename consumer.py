from multiprocessing import Queue, Process


class Consumer(Process):
    def __init__(self, queue: Queue):
        super(Consumer, self)
        self.queue = queue
        pass

    def run(self):
        while True:
            self.consume()

    def consume(self):
        pass
