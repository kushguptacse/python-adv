class Example2:
    class_var = 4

    @staticmethod
    def static_method(arg1, arg2):
        print(arg1, arg2, Example2.class_var)

    @staticmethod
    def static_method2():
        print("hello")


print(Example2.class_var)  # 4
Example2.static_method(2, 3)  # 2 3 4
Example2.static_method2()  # hello
