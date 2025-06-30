

def decorator(func):
    def func_sq(func):
        print( "func is fucking")
        func
        print("its an wrpper")
    
    return func_sq(func)


@decorator
def func(a,b):
    return a+b

print(func(2,3))