class Example:
    class_var = 4

    def __init__(self):
        print("inside init")
        self.ins_var = "kk"

    def ins_method(self):
        print(self.ins_var, self.class_var, Example.class_var)


print(Example.class_var)  # 4
obj = Example()  # inside init
print(obj.ins_var)  # kk
obj.ins_method()  # kk 4 4
