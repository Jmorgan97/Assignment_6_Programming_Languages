import multiprocessing as mp
import sys
from threading import RLock
from time import sleep
from signal import signal, SIGINT, SIG_IGN
from producer import Producer
from consumer import Consumer

pro_resource = 3
con_resource = 4
lock = RLock()

def main():
    global con_resource
    global pro_resource
    queue = mp.Queue()
    processes = [Producer(queue, i, lock) for i in range(pro_resource)]
    processes.extend([Consumer(queue, i, lock) for i in range(con_resource)])

    # Create 3 producers and 4 consumers


    # Begin execution of each of the different
    for p in processes:
        p.daemon = True
        p.start()
    try:
        while True:
            sleep(0.5)
    except KeyboardInterrupt:
        print("\nProgram terminated")
        sys.exit(0)


if __name__ == '__main__':
    main()
