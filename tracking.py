import os
import datetime
import time

timestamp = datetime.datetime.now()

# The method to convert timestamp from string to date to compare
#
# datetime.datetime.strptime("2020-03-02 02:22:47.105655", '%Y-%m-%d %H:%M:%S.%f'):


def todayAt(hr=0, min=0, sec=0, micros=0):
    now = datetime.datetime.now()
    return now.replace(hour=hr, minute=min, second=sec, microsecond=micros)


def followadd(user):

    if os.path.exists("peoplefollowed.txt"):
        write_append = "a"
    else:
        write_append = "w"

    followlist = open("peoplefollowed.txt", write_append)
    followlist.write(user + " " + str(timestamp) + "  " + str(time.time()) + "\n")
    followlist.close()


def followremove(user):

    with open("peoplefollowed.txt") as file:
        lines = file.readlines()
    with open("peoplefollowed.txt", "w") as file:
        for line in lines:
            if not line.startswith(user + " "):
                file.write(line)

def checkAge():
    listofnames = []
    with open("peoplefollowed.txt") as file:
        lines = file.readlines()
        for line in lines:
            date = line.split("  ", 1)
            user = line.split(" ", 1)
            if float(time.time()) > float(date[1]) + 432000:
                listofnames.append(user[0])

    return listofnames


# if __name__ == "__main__":
