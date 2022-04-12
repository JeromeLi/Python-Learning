import time

def hello():
    time.sleep(1)

def run():
    for i in range(10):
        hello()
        print('Hello World! : %s' % time.ctime() )

if __name__ == '__main__':
    run()
