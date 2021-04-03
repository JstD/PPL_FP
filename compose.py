from functools import reduce
def compose(*args):
    def inner(x):
        return reduce(lambda x,y: y(x),args[::-1],x)
    return inner
increase= lambda x: x+1
square = lambda x : x*x
f = compose(increase,square)

print(f(3)) #increase(square(3)) = 10
