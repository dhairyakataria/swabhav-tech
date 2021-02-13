
x = 10
def update(val):
    print(id(val))
    val = 0
    print(id(val))

update(x)
print(x)