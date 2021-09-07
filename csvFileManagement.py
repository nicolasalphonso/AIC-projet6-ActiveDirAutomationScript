import csv
from tkinter import filedialog

'''
This function manages data reading from csv file
'''


def open_csv_file():
    # open csv file and retrieve data
    filename = filedialog.askopenfilename()
    data = open(filename, encoding="utf-8")
    csv_data = csv.reader(data)
    data_lines = list(csv_data)

    # print filename
    print('Selected File:', filename)

    # return data lines
    return data_lines
