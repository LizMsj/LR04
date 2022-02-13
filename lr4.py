import os

def pt():
    x = input('Введите путь к папке: ')
    if os.path.isdir(x) == True:
        print('Проведён анализ в папке ', x, '\n')
        return x
    else: pt(d1)
  
def dictionary(x):
    d1 = {}
    for filename in os.listdir(x):
        current_puth = os.path.join(x, filename)
        if os.path.isdir(current_puth):
            d1.update(dictionary(current_puth))
        else:
            d1[current_puth] = os.path.getsize(current_puth)
    return d1
    
def duble(d1):
    big_dict = {}
    for way, size in d1.items():
        name = str(os.path.basename(way)) + '_' + str(size)
        if (name) in big_dict.keys():
            big_dict.get(name).append(way)
        else:
            big_dict[name]=[way]
    d1.clear()
    for name, filesize in big_dict.items():
        if len(filesize) > 1:
            d1[name] = filesize
    return d1

def fin(d1):
    if len(d1)==0:
        print('Дубликатов нет')
    else:
        for filename, ways in d1.items():
            size = os.path.getsize(ways[0])
            print(size)
            for x in ways:
                print(x)
            print()
  
if __name__ == '__main__':
    fin(duble(dictionary(pt())))
