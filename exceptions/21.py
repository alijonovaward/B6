def f(d:dict,key:str,value):
    try:
        if not isinstance(d, dict):
            raise TypeError("Dict emas")
        d[key]=value
        return d
    except TypeError:
      print()

print(f([1, 2],"name","Asror"))