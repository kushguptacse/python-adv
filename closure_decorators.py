def outer(msg:str)->None:
    var1 = "hello"
    var2 = f"{var1} {msg}"
    def inner():
        print(var2)
    inner()

outer("kush")
