powGen = lambda x: lambda y: y**x
square = powGen(2)
print(square(3))