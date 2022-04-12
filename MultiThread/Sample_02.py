import sys, time, subprocess

timeLeft = 10

while timeLeft > 0:
    sys.stdout.write("ETA: %s" % timeLeft)
    sys.stdout.flush()
    # print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

subprocess.Popen(['open', 'alarm.wav'])

