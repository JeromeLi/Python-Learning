# import time, datetime

# startTime =  datetime.datetime(2030, 10, 31, 0, 0, 0)
# while datetime.datetime.now() < startTime:
#     time.sleep(1)
#     print(datetime.datetime.now().strftime("%Y-%b-%d (%a) %H:%M:%S"))

# print('Program now starting on New Year 2030')

import threading, time, datetime

print('Start of program.')

def takeANap():
    startTime =  datetime.datetime.now().strftime("%Y-%b-%d (%a) %H:%M:%S")
    print('start time is:', startTime)
    time.sleep(5)
    print('Wake Up!')
    endTime =  datetime.datetime.now().strftime("%Y-%b-%d (%a) %H:%M:%S")
    print('end time is:', endTime)


threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program.')
