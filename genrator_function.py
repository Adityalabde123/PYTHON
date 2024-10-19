def show():
    yield 1
    yield 22
    yield 33
    yield 22
for i in show():
    print(i)