from os import *

def pt():
    x = input('Введите путь к папке: ')
    if path.isdir(x) == True:
        print("Проведён анализ в папке ", x)
        dictionary(x)
    else: pt()
  
def dictionary(x):
    for i in listdir(x):
        if path.isdir(x + "\\" + i):
            dictionary(x+ '\\' + i)
        elif path.isfile(x + '\\' + i):
            name = x + "\\" + i
            size = stat(x + "\\" + i).st_size
            d1[name] = size
            A.append(i)
    return d1, A

def duble(d1, A):
    size = list(d1.values())
    pop = list(d1.keys())
    D = [i for i, x in enumerate(size) if size.count(x) > 1]
    D1 = [i for i, x in enumerate(A) if A.count(x) > 1]
    index = []
    d1.clear()
    help_in_way = []
    if len(D) >= len(D1):
        for x in D:
            if x in D1:
                index.append(x)
    else:
        for x in D1:
            if x in D:
                index.append(x)
    for x in index:
        t = [A[x], size[x]]
        d1[pop[x]]= t
        help_in_way.append(A[x])
    fin(d1)

def fin(d1):
    print()
    if len(d1)==0:
        print("Дубликатов нет")
    else:
        help_in_way = list()
        for x in d1.values():
            if x not in help_in_way:
                help_in_way.append(x)
        help_in_way.sort()
        for y in help_in_way:
            print("Дубликаты ", y)
            p = [k for k in d1 if d1[k] == y]
            for i in p:
                print(str(i).replace("\\\\", "\\"))
            print()
  
if __name__ == '__main__':
    d1 = dict() # словарь - ключ (путь до файла): значение(размер файла)
    pt()
    duble(d1, A)
    
