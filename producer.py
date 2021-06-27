from multiprocessing import Queue, Process
import random

class Producer(Process):
  def __init__(self, name, queue: Queue): #initialize the Producer Class
    super(Producer, self)
    self.name = name        #initialize a producer Class object with a name, ex. Producer 1, Producer 2, etc.
    self.queue = queue
    self.items = ["banana", "apple", "orange", "grapefruit", "tangerine", "clementine", "pear", "grapes", 
                    "strawberries", "raspberries", "blackberries", "blueberries", "cherries", "kiwi", "dragonfruit", 
                    "starfruit", "papaya", "mango", "peach", "pineapple", "cantaloupe", "watermelon", "lime", "lemon", 
                    "plum", "avocado", "tomato", "onion", "garlic", "potato", "radish", "brocolli", "carrot", "asparagus", 
                    "green onions", "spinach", "bell pepper", "iceburg lettuce", "romain lettuce", "cucumber", "celery", 
                    "corn", "mushrooms", "cabbage", "green beans", "peas", "cauliflower"] 
                 #array of strings of item names that can be grabbed from to generate items
                 #haha all of the items are produce, get it? :^>
        
  def proGet(self): #method to grab a random item from the items list to pass along to another class via a function call
        randomItem = random.choice(self.items)
        return randomItem
 
#testrun instructions
p1 = Producer("Producer 1") #create a producer for test
print(p1.name,"has generated:", p1.proGet()) #test case print output
