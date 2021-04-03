from functools import reduce
flatten = lambda lst:list(reduce(lambda x,y:x+y,lst,[]))
print(flatten([[1,2,3],[4,5],[6,7]]))
