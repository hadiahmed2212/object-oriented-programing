class employee:
    def __init__(self):
        print("employee hired")
    def __del__(self):
        print("employee fired")

def crt_obj():
    print("making object-_-")
    obj=employee()
    print("function ending :)")
    return obj
print("calling function:D")
obj= crt_obj()
print("bye,program ended")
