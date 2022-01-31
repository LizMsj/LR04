def pt():
    x = input('Введите путь к папке: ')
    if path.isdir(x) == True:
        print("Проведён анализ в папке ", x)
        dictionary(x)
    else: pt()
  
def dictionary(x):
    for i in listdir(x):
        if path.isdir(x + "\\" + i):
            dictionary(x+ '\\' + i, level+1)
        elif path.isfile(x + '\\' + i):
            name = x + "\\" + i
            size = stat(x + "\\" + i).st_size
            d1[name] = size
            A.append(i)
    return d1, A

def duble():
    pass

def fin():
    pass
  
if __name__ == '__main__':
    d1 = dict() # словарь - ключ (путь до файла): значение(размер файла)
    pt()
    
