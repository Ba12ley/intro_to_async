import string
import time
import threading


def main():
    # # Set the target function to thread, add args and daemon thread to run in background
    # t1 = threading.Thread(target=greeting, args=('paulo', 10), daemon=True)
    # t2 = threading.Thread(target=numbers, daemon=True)
    # t3 = threading.Thread(target=letters, daemon=True)
    # print('Thread running')
    # # Start the thread
    # t1.start()
    # t2.start()
    # t3.start()
    #
    # # To ensure the thread ends join when finished
    # t1.join()
    # t2.join()
    # t3.join()
    # Or create a list of threads
    threads = [threading.Thread(target=greeting, args=('paulo', 10), daemon=True),
               threading.Thread(target=numbers, daemon=True),
               threading.Thread(target=letters, daemon=True)]
    # List comprehension
    [t.start() for t in threads]
    # List comprehension, use timeout to end thread after number of cycles
    [t.join(timeout=1) for t in threads]


def greeting(name: str, times: int):
    for i in range(0, times):
        print(f'{i} Hi {name}')
        time.sleep(1)


def numbers():
    for i in range(0, 20):
        print(f'{i} waiting 2 seconds')
        time.sleep(2)


def letters():
    letters = string.ascii_letters
    for letter in letters:
        print(f"{letter} wait 0.5 seconds")
        time.sleep(0.5)


if __name__ == '__main__':
    main()
