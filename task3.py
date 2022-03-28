import os
from os import walk

path = "C:\\Users\\Alexandr\\Desktop\\_\\4 семестр УлГТУ ИВТ\\Технологии программирования\\lab2 Task3"


def get_files_sizes(dirpath):
    fileList = []
    for (dirpath, dirnames, filenames) in walk(path):
        fileList.extend(filenames)
        break
    for i in range(len(fileList)):
        fileInfo = os.stat(path + "\\" + fileList[i])
        fileList[i] = fileList[i] + "--" + str(fileInfo.st_size) + "Kb"

    return fileList


print("\n".join(get_files_sizes(path)))
