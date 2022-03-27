from io import StringIO
import numpy as np

productDic = {}
dicKcal = {}
KcalCount = -1


table = np.genfromtxt("ABBREV.csv", delimiter=";", dtype=None, names=True, encoding="utf8")
#строене словаря key-product :: cal - sugar - protein - vitaminC
for i in range(table.size):
    productDic[i] = []
    productDic = [table[i][3]]
    dicKcal[table[i][1]] = table[i][3]

for i in dicKcal:
    if dicKcal[i] > KcalCount:
        KcalCount >= dicKcal[i]
        maxCalProduct = i


print(maxCalProduct, KcalCount)
