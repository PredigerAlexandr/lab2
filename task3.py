import json
import os
from operator import itemgetter
from os import walk
import re

import numpy as np
import csv


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


###
def sortedCSV(path, column):
    result = ''
    listString = []
    with open(path) as File:
        reader = csv.reader(File)
        for row in reader:
            listString.append(str(row).split(";"))
    listString.pop(0)
    outputList = sorted(listString, key=lambda x: x[column])
    for i in outputList:
        result = result + str(i) + "\n"
    return result


###
def readCsv(path):
    result = ""
    with open(path) as File:
        reader = csv.reader(File)
        for row in reader:
            result += (str(row) + "\n")
    return result


###
def sortedByAttribute(path):
    glistString = []
    result = ''
    with open(path) as File:
        reader = csv.reader(File)
        for row in reader:
            glistString.append(str(row).split(";"))
    glistString.pop(0)
    lenMas = len(glistString)
    iter = 0
    while (iter < lenMas):
        if 'true' not in glistString[iter]:
            glistString.pop(iter)
            lenMas -= 1
            iter -= 1
        iter += 1
    for i in glistString:
        result = result + str(i) + '\n'
    return result


##
def createJson(sortedCsvFile, path):
    jsonFile = sortedCsvFile
    chunks = re.split('\[\"\[\'|\", \'|\'\]\"\]\n|\'|, |\"', jsonFile)
    iter = 0
    while iter != len(chunks):
        if chunks[iter] == '':
            chunks.pop(iter)
            iter -= 1
        iter += 1
    iter = 0
    output = []
    while iter != len(chunks):
        dic = {"№": int(chunks[iter]), "date/time": chunks[iter + 1], "output/input": bool(chunks[iter + 2]),
               "sex": chunks[iter + 3]}
        output.append(dic)
        iter += 4
    with open(path + "\\end.json", 'w') as outfile:
        json.dump(output, outfile)
    print(".json file successfully created")


path = "C:\\Users\\Alexandr\\Desktop\\_\\4 семестр УлГТУ ИВТ\\Технологии программирования\\lab2 Task3"
csvFileFlag = False

print("\n".join(get_files_sizes(path)))

if csvFileFlag:
    fileCsv = path + "\\" + input("Enter the CSV name of the file, wich you want to see:")
    print(readCsv(fileCsv))
    print("You have 2 attempts for sorting thr csv file")
    for i in range(2):
        column = int(input("Enter the column by wich you want to sorting:"))
        print(sortedCSV(fileCsv, column))
    createJson(sortedByAttribute(fileCsv),path)
else: print(".csv file is miss")
