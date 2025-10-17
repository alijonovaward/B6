def download():
    return "fail"


try:
    data = download()
    if data == "fail":
        raise Exception("No internet")
    print(data)
except:
    print("Yuklashda xatolik, Check the network")
