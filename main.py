from objects import DatapointCollection
import multiprocessing as mp
import time


def receive_collection(flag: mp.Event):
    while True:
        flag.wait()
        datapoint_collection = None
        print(f'Received collection {datapoint_collection.checksum()}')
        flag.clear()
        time.sleep(1)


def spawn_collection(flag: mp.Event):
    while True:
        datapoint_collection = DatapointCollection(1_000_000)
        print(f'Spawned collection {datapoint_collection.checksum()}')
        flag.set()
        time.sleep(1)


def main():

    flag = mp.Event()

    spawner = mp.Process(target=spawn_collection, args=(flag,))
    receiver = mp.Process(target=receive_collection, args=(flag,))

    spawner.start()
    receiver.start()

    spawner.join()
    receiver.join()


if __name__ == '__main__':
    main()
