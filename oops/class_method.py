class Example:
    class_var = 4
    def __init__(self):
        print("inside init")
        self.ins_var = "kk"

    @classmethod
    def class_method(cls):
        print(cls.class_var)
        #print(cls.ins_var) not available

print(Example.class_var) #4
Example.class_method() #4
obj = Example() # inside init
print(obj.ins_var) #kk
obj.class_method() #4