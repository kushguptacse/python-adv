class PowerOf2:
    def __init__(self, size):
        self.size = size

    def __iter__(self):
        self.i = 1
        return self

    def __next__(self):
        if self.i <= self.size:
            pow = self.i**2
            self.i += 1
            return pow
        else:
            raise StopIteration


for item in PowerOf2(10):
    print(item) # print square of numbers from 1 till 10

op = [pow for pow in PowerOf2(10)] #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(op)

def generator(size):
    i=1
    while i<=size:
        yield i**2
        i+=1

print("generator example")
g = generator(10)

for item in g:
    print(item)