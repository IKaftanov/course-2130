
def fibonacci():
   
    if not hasattr(f, 'x'):
        f.x = 0
        return f.x
    if not hasattr(f, 'y'):
        f.y = 1
        return f.y
    z = f.x + f.y
    f.x = f.y
    f.y = z
    return z


def f():
    if not hasattr(f, 'x'):
        f.x = 0
    f.x += 1
    return f.x


for i in range(10):
    print(fibonacci())
      
