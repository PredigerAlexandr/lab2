import os
from os import walk
import numpy as np

path = "C:\\Users\\Alexandr\\Desktop\\_\\4 семестр УлГТУ ИВТ\\Технологии программирования\\lab2 Task3"
csvFileFlag = False


def get_files_sizes(dirpath):
    global csvFileFlag
    fileList = []
    for (dirpath, dirnames, filenames) in walk(path):
        fileList.extend(filenames)
        break
    for i in range(len(fileList)):
        if ".csv" in fileList[i]:
           csvFileFlag = True
        fileInfo = os.stat(path + "\\" + fileList[i])
        fileList[i] = fileList[i] + "--" + str(fileInfo.st_size) + "Kb"

    return fileList
file = open("C:\\Users\\Alexandr\\Desktop\\_\\4 семестр УлГТУ ИВТ\\Технологии программирования\\lab2 Task3\\Clients.csv")

print("\n".join(get_files_sizes(path)))

if csvFileFlag:
    # fileCsv = input("Enter the CSV name of the file, wich you want to see:")
    # print(path+"\\"+fileCsv)
    table = np.genfromtxt(file, delimiter=";", dtype=None, names=True, encoding="utf8")
    print(table)
    # print(np.sort(table, axis=None))
    typer = np.dtype([('№', 'U8'), ('date/time', 'U8'), ('output/input', 'U8'), ('sex', "U8")])
    table2 = np.array(table, dtype=typer)
    print(np.sort(table2, order='sex'))

# type = np.dtype([('recruit_name', 'U8'), ('age', int),('weight', float), ('height', float)])
# recruit = [('Вася', 18, 57.1, 1.96),('Петька', 25, 94.9, 1.51),('Сёмка', 30, 72.5, 1.83),('Антоха', 30, 146.8, 1.76)]
# vdv = np.array(recruit, dtype=type)
# print(vdv)
# print(np.sort(vdv, order='recruit_name'))  # сортировка по весу

