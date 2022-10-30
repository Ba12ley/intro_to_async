import time
import threading


def main():
    t = threading.Thread(target=greeting, args=('paulo', 10), daemon=True)
    t.start()
    print()
    print('Thread running')
    numbers()
    print()
    print(9*9)
    t.join()
    # greeting('Mark', 10)

def greeting(name: str, times: int):
    for i in range(0,times):
        print(f'{i} Hi {name}')
        time.sleep(1)

def numbers():
    for i in range(0,20):
        print(i)
        time.sleep(2)

if __name__ == '__main__':
    main()