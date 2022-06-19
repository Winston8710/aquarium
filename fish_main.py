from threading import *
import dist5
import wetinsql

if __name__ =="__main__":
    threads =[]
    threads.append(Thread(target = dist5.distt))
    threads.append(Thread(target = wetinsql.wet))

    for t in threads:
        t.start()
    for t in threads:
        t.join()