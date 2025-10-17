def main(l:list):
    try:
        for i in l:
            if not isinstance(i, int):
                raise TypeError()
            #else :
             #   print(i)
        print("sum : ", sum(l))
    except TypeError:
        print("son bo`lmagan elemnet aniqlandi")
main([1, 2, 3, 4, 5, "3"])