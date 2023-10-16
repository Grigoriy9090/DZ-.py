stroka = ('пара-ра-рам рам-пам-папам па-ра-па-дам')
list2 = stroka.split()
res = []
count = 0
for el1 in list2:
    for el2 in el1:
        if el2 in stroka:
            count += 1
        res.append(count)
        count = 0
res_char = res[0]
if all(map(lambda a: a == res_char, res)) and len(res) - 1 > 0:
    print('Парам пам-пам')
elif len(res) - 1 == 0:
    print('количество фраз должно быть больше одной! ')
else:
    print('Пам парам')