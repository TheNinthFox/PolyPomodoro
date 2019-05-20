import os
import sys
import math
import time
import datetime


def parse_commands(file_path):
    try:
        command = sys.argv[1]

        if command == "start":
            with open(file_path, "w") as data:
                start_time = datetime.datetime.now().timestamp()
                data.write(f"{start_time}")
                os.system('notify-send "Pomodoro started for 25 minutes"')
                sys.exit(0)
        if command == "stop":
            os.remove(file_path)
            os.system('notify-send "Pomodoro stopped"')
            sys.exit(0)
    except Exception as e:
        #print(e)
        pass


def load_start_time(start_time, file_path):
    if start_time < 0:
        with open(file_path, "r") as data:
            start_time = float(data.read())
            return start_time


def process(start_time, file_path):
    time_passed = datetime.datetime.now().timestamp() - start_time
    time_left = work_duration - time_passed
    minutes = math.floor(time_left / 60)
    seconds = math.floor(time_left - (minutes * 60))

    if time_left <= 0:
        os.remove(file_path)
        os.system('notify-send "Pomodoro done. Take a break!"')
        print(" ready")
        sys.exit(0)

    print(f" {minutes:02d}:{seconds:02d}")


if __name__ == '__main__':
    file_path = "/home/fox/.cache/pomodoro"
    work_duration = 25 * 60
    start_time = -1

    parse_commands(file_path)

    # We are not running
    if not os.path.isfile(file_path):
        print(" ready")
        sys.exit(0)

    start_time = load_start_time(start_time, file_path)

    process(start_time, file_path)
