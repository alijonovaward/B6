# def decorator(func:callable):
#     count = 0
#     def wrapper(*args):
#         nonlocal count
#         count += 1
#         if count < 6:
#             func(*args)
#         else:
#             print("Siz 5 marta fo...")
#             return
#
#     return wrapper
#
#
#
# @decorator
# def myfunc(*n):
#     print(n)
#
#
# myfunc(1)
# myfunc(1)
# myfunc(1)
# myfunc(1)
# myfunc(1)
# myfunc(1)





def limit(n:int):
    def decorator(func:callable):
        count = 0
        def wrapper(*args):
            nonlocal count
            count += 1
            if count <= n:
                func(*args)
            else:
                print(f"Siz {n} marta f...")


        return wrapper
    return decorator

@limit(2)
def hello():
    print("hello")

hello()
hello()
hello()