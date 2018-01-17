import threading
import time

total = 4
lock = threading.Lock()


def create_item_1():
    global total
    for i in range(10):
        time.sleep(1)
        with lock:
            total += 1
            print("creator_1 add item to {}".format(total))
    print("Creator_1 FINISHED JOB")


def create_item_2():
    global total
    for i in range(7):
        time.sleep(1)
        with lock:
            total += 1
            print("creator_2 add item to {}".format(total))
    print("Creator_2 FINISHED JOB")


def limit_item():
    global total
    while True:
        if total > 5:
            with lock:
                print('total is {},subtracted 3'.format(total))
                total -= 3
        else:
            time.sleep(1)
            with lock:
                print('waiting for 1 second')


creator_1 = threading.Thread(target=create_item_1)
creator_2 = threading.Thread(target=create_item_2)
limitor = threading.Thread(target=limit_item, daemon=True)

creator_1.start()
creator_2.start()
limitor.start()

creator_1.join()
creator_2.join()


print("OUR ENDING VALUE IS {}".format(total))



