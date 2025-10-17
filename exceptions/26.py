def getVal(lst: list, index: int):
    try:
        print(lst[index])
    except IndexError:
        print("Error")
    except TypeError:
        print("index must be int")

l = [1, 2, 3]

getVal(l, -1)