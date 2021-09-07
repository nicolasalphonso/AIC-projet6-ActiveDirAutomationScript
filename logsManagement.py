import os

'''
This function prints and writes the logs to a txt file in logs folder
'''


def write_logs(logs, initial_log, initial_time, type):
    # if no log was written, just add "Nothing to declare" in the log file
    if logs == initial_log:
        logs += "\n Nothing to declare ! :)"
    print(logs)

    # create the logs directory if it doesn't exist
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # create the log file in logs folder
    log_file_name = "logs/" + type + "_" + initial_time + ".txt"
    file = open(log_file_name, "a")
    file.write(logs)
    file.close()
