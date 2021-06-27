from multiprocessing import Queue
from threading import Thread, RLock
import random
import time


class Producer(Thread):
    def __init__(self, queue: Queue, idx: int, glock: RLock):
        super(Producer, self).__init__()
        self.queue = queue
        self.idx = idx
        self.sleep = lambda: random.random() * 2
        self.lock = glock
        self.items = ["banana", "apple", "orange", "grapefruit", "tangerine",
                      "clementine", "pear", "grapes", "strawberries",
                      "raspberries", "blackberries", "blueberries", "cherries",
                      "kiwi", "dragonfruit", "starfruit", "papaya", "mango",
                      "peach", "pineapple", "cantaloupe", "watermelon", "lime",
                      "lemon", "plum", "avocado", "tomato", "onion", "garlic",
                      "potato", "radish", "brocolli", "carrot", "asparagus",
                      "green onions", "spinach", "bell pepper",
                      "iceburg lettuce", "romain lettuce", "cucumber",
                      "celery", "corn", "mushrooms", "cabbage", "green beans",
                      "peas", "cauliflower"]
    # array of strings of item names that can be grabbed from to generate items
    # haha all of the items are produce, get it? :^>

    def run(self):
        try:
            while True:
                with self.lock:
                    print(f"Producer({self.idx}): Placing in queue")
                self.queue.put(self.proGet())
                time.sleep(self.sleep())
        except KeyboardInterrupt:
            return
    # method to grab a random item from list to put into queue
    def proGet(self):
        randomItem = random.choice(self.items)
        return randomItem
