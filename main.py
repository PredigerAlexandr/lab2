from operator import itemgetter

import numpy
import numpy as np

productDic = {}
KcalCount = -1
sugarCount = 999999999
proteinCount = -1
vitaminCcount = -1

table = np.genfromtxt("ABBREV.csv", delimiter=";", names=True, dtype=None, encoding="utf8")
productList = []

sortedAr = np.sort(table, order='Energ_Kcal')
print(sortedAr[sortedAr.size - 1][1], "-", sortedAr[sortedAr.size - 1][3])
print(min(table, key=itemgetter(9))[1], '-', min(table, key=itemgetter(9))[9])
print(max(table, key=itemgetter(4))[1], '-', max(table, key=itemgetter(4))[4])
print(max(table, key=itemgetter(20))[1], '-', max(table, key=itemgetter(20))[20])

