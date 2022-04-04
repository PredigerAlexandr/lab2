from io import StringIO

import numpy
import numpy as np

productDic = {}
KcalCount = -1
sugarCount = 999999999
proteinCount = -1
vitaminCcount = -1

table = np.genfromtxt("ABBREV.csv", delimiter=";", dtype=None, names=True, encoding="utf8")
productList = []

# строене словаря key-product :: cal - sugar - protein - vitaminC
for i in range(table.size):
    productDic[table[i][1]] = [table[i][3], table[i][9], table[i][4], table[i][20]]
    productList.append([table[i][1], table[i][3], table[i][9], table[i][4], table[i][20]])

# for i in range(len(productList)):
#     print(type(productList[i][0]))
typer = np.dtype([('Product', 'U8',16), ('Cal', 'U8'), ('sugar', 'U8'), ('protein', 'U8'), ('vitaminC', 'U8')])
productAr = np.array(productList, dtype=typer)
np.sort(productAr, order = 'Cal')
print(productAr[1][1])



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
