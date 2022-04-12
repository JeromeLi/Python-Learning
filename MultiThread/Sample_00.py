import time, datetime

startTime =  datetime.datetime(2030, 10, 31, 0, 0, 0)
while datetime.datetime.now() < startTime:
    time.sleep(1)
    print(datetime.datetime.now().strftime("%Y-%b-%d (%a) %H:%M:%S"))

print('Program now starting on New Year 2030')
