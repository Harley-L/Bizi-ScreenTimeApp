# Imports
import time
import subprocess

# Global Variables
interval = 2  # Set the time interval between screen checks
openapps = []  # Second set to move set to list (Easier to work with)
todayapps = [["Total Time", -interval]]  # All time spent on an app on the present day
# Passive apps
passiveapps = ["-----------", "Description", "Application Frame Host", "Settings","Cortana","Store"]


def outputtolist():
    global openapps
    openapps = []
    cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    for line in proc.stdout:
        if line.rstrip():
            # only print lines that are not empty
            # decode() is necessary to get rid of the binary string (b')
            # rstrip() to remove \r\n
            # print(line.decode().rstrip())
            p = line.decode().rstrip()
            k = 1  # Kill switch
            for app in passiveapps:
                if p == app:
                    k = 0
            if k == 1:
                openapps.append(p)
    pass


def updateapps():
    todayapps[0][1] += interval
    for app in openapps:  # Add apps to the list if not on the list AND add time to apps that are already on the list
        s = 1
        for i in range(len(todayapps)):
            if todayapps[i][0] == app:  # If already on the list add time
                todayapps[i][1] += interval
                s = 0
        if s == 1:
            todayapps.append([app, 0])  # If not on the list add to list with time 0
    pass


def main():

    outputtolist()
    updateapps()
    print(todayapps)

    # Interval time and Recursion
    time.sleep(interval)
    main()  # recursion

main()

# Tasklist:
# At the end of the day, export todaysapps to a file
# Maybe change the time mechanic noting time open/time closed
# add mechanic of what screen you are actually on.
# What UI library will we use
