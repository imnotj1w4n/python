def A( ):
    print(1)
    r=B()
    print(r)
def B( ):
    print(2)
    return 3

A()
print(4)
