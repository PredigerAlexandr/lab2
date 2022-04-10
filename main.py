from io import StringIO
from operator import itemgetter

import numpy
import numpy as np

productDic = {}
KcalCount = -1
sugarCount = 999999999
proteinCount = -1
vitaminCcount = -1

table = np.genfromtxt("ABBREV.csv", delimiter=";", names = True, dtype=None, encoding="utf8")
productList = []

sortedAr = np.sort(table, order='Energ_Kcal')
print(sortedAr[sortedAr.size-1][1], "-", sortedAr[sortedAr.size-1][3])
print(min(table, key=itemgetter(9))[1],'-', min(table, key=itemgetter(9))[9])
print(max(table, key=itemgetter(4))[1],'-', max(table, key=itemgetter(4))[4])
print(max(table, key=itemgetter(20))[1],'-', max(table, key=itemgetter(20))[20])





















# # строене словаря key-product :: cal - sugar - protein - vitaminC
# for i in range(table.size):
#     productDic[table[i][1]] = [table[i][3], table[i][9], table[i][4], table[i][20]]
#
#
# print()
# for i in productDic:
#     if productDic[i][0] >= KcalCount:
#         KcalCount = productDic[i][0]
#         maxCalProduct = i + " -- " + str(KcalCount)
#
#     if productDic[i][1] < sugarCount:
#         sugarCount = productDic[i][1]
#         minSugarCount = i + " -- " + str(sugarCount)
#
#     if productDic[i][2] > proteinCount:
#         proteinCount = productDic[i][2]
#         maxProteinProduct = i + " -- " + str(proteinCount)
#
#     if productDic[i][3] > vitaminCcount:
#         vitaminCcount = productDic[i][3]
#         maxVitaminCProduct = i + " -- " + str(vitaminCcount)
#
# print(maxCalProduct, minSugarCount, maxProteinProduct, maxVitaminCProduct, sep='\n')
