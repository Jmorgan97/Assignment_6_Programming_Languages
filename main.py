import multiprocessing as mp
from time import sleep
from signal import signal, SIGINT, SIG_IGN
from Producer import Producer
from Consumer import Consumer

pro_resource = 3
con_resource = 4


# Acts to initialize the environemnt by listening for SIGINT so our program
# can instead process it rather than the kernel.
def initialize_signals():
    signal(SIGINT, SIG_IGN)


def main():
    global con_resource
    global pro_resource
    initialize_signals()
    queue = mp.Queue()
    processes = [Producer(queue) for i in range(pro_resource)]
    processes.extend([Consumer(queue) for i in range(con_resource)])
    # Create 3 producers and 4 consumers

    try:
        # Begin execution of each of the different
        for p in processes:
            p.start()
        while True:
            sleep(0.5)
    except KeyboardInterrupt:
        for p in processes:
            p.terminate()
            print("Program terminated")
            exit(0)



if __name__ == '__main__':
    main()
