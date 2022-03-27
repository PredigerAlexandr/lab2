from io import StringIO
import numpy as np

productDic = {}
KcalCount = -1
sugarCount = 999999999
proteinCount = -1
vitaminCcount = -1

table = np.genfromtxt("ABBREV.csv", delimiter=";", dtype=None, names=True, encoding="utf8")

# строене словаря key-product :: cal - sugar - protein - vitaminC
for i in range(table.size):
    productDic[table[i][1]] = [table[i][3], table[i][9], table[i][4], table[i][20]]

for i in productDic:
    if productDic[i][0] >= KcalCount:
        KcalCount = productDic[i][0]
        maxCalProduct = i + " -- " + str(KcalCount)

    if productDic[i][1] < sugarCount:
        sugarCount = productDic[i][1]
        minSugarCount = i + " -- " + str(sugarCount)

    if productDic[i][2] > proteinCount:
        proteinCount = productDic[i][2]
        maxProteinProduct = i + " -- " + str(proteinCount)

    if productDic[i][3] > vitaminCcount:
        vitaminCcount = productDic[i][3]
        maxVitaminCProduct = i + " -- " + str(vitaminCcount)

print(maxCalProduct, minSugarCount, maxProteinProduct, maxVitaminCProduct, sep='\n')
