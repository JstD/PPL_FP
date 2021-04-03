def flatten(lst):
    if not lst:
        return []
    return lst[0]+ flatten(lst[1:])

print(flatten([[1,2,3],[4,5],[6,7]]))