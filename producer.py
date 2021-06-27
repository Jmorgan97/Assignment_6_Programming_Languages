from multiprocessing import Queue, Process
import random


class Producer(Process):
    def __init__(self, queue: Queue, idx: int):
        super(Producer, self)
        self.queue = queue
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
        while True:
            self.queue.put(self.proGet)

    # method to grab a random item from list to put into queue
    def proGet(self):
        randomItem = random.choice(self.items)
        return randomItem
