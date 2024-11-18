"""from itertools import combinations  -------- ПЕРВЫЙ ВАРИАНТ РЕШЕНИЯ, НО ПРОГРАММА ВЫВОДИТ ВСЕ ПОДПОСЛЕДОВАТЕЛЬНОСТИ
                                                                                                                СТРОКИ


def all_variants(text):
    for k in range(1, len(text) + 1):
        for elem in combinations(text, k):
            yield ''.join(elem)


obj = all_variants('abc')
for i in obj:
    print(i)"""


def all_variants(text):
    for st in range(1, len(text) + 1):
        for p in range(len(text) - st + 1):
            if p + st <= len(text):
                yield text[p:p + st]


obj = all_variants('abcdef')
for i in obj:
    print(i)
