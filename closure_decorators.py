def outer(msg: str) -> None:
    var1 = "hello"
    var2 = f"{var1} {msg}"
    def inner():
        print(var2)
    inner()

outer("kush")


def debug(fn):
    def debugger(*args, **kwargs):
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        print(f"Function {fn.__name__} called")
        fn_result = fn(*args, **kwargs)
        print(f"Function {fn.__name__} returns: {fn_result}")
        return fn_result

    return debugger


@debug
def something(a, b, c=0,d=4):
    return a + b if c!=0 else d

something(1, b=2,c=3)
# Args: (1,)
# Kwargs: {'b': 2, 'c': 3}
# Function something called
# Function something returns: 3

@debug
def something2(*a, **kwargs):
    return f"{a}, {kwargs}"

something2(1,2,3,k=2)

# Args: (1, 2, 3)
# Kwargs: {'k': 2}
# Function something2 called
# Function something2 returns: (1, 2, 3), {'k': 2}

def timer(fn):
    import time
    def process_time(*args,**kwargs):
        print("Start timer!")
        start_time = time.perf_counter()
        fn_result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        time_duration = end_time - start_time
        print(f"Function {fn.__name__} took: {time_duration} s")
        return fn_result
    
    return process_time

@debug
@timer
def my_function(name: str) -> None:
    print(f"Hello: {name}")

my_function("hello")

# Args: ('hello',)
# Kwargs: {}
# Function process_time called
# Start timer!
# Hello: hello
# Function my_function took: 1.3018998288316652e-05 s
# Function process_time returns: None