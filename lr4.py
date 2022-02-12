import os

def pt():
    x = input('Введите путь к папке: ')
    if os.path.isdir(x) == True:
        print('Проведён анализ в папке ', x, '\n')
        dictionary(x)
    else: pt()
  
def dictionary(x):
    for filename in os.listdir(x):
        current_puth = os.path.join(x, filename)
        if os.path.isdir(current_puth):
            d1.update(dictionary(current_puth))
        else:
            d1[current_puth] = os.path.getsize(current_puth)
    return d1
    

def duble(d1: dict):
    big_dict = {}
    for way, size in d1.items():
        name = str(os.path.basename(way) + '_' + str(size))
        if (name) in big_dict.keys():
            big_dict.get(name).append(way)
        else:
            big_dict[name]=[way]
    d1.clear()
    for name, filesize in big_dict.items():
        if len(filesize) > 1:
            d1[name] = filesize
    fin(d1)

def fin(d1):
    if len(d1)==0:
        print('Дубликатов нет')
    else:
        for filename, ways in d1.items():
            print('Дубликат типа "' + filename + '":')
            for way in ways:
                print(way)
            print()
  
if __name__ == '__main__':
    d1 = {}
    pt()
    duble(d1)
