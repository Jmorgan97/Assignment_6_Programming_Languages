from multiprocessing import Queue, Process


class Producer(Process):
    def __init__(self, queue: Queue):
        super(Producer, self)
        # Boilerplate, so I can make the main class
        self.item = None
        self.queue = queue
        pass

    # Rely on main process to end this child process
    def run(self):
        while True:
            self.produce()
        pass

    def produce(self):
        pass
