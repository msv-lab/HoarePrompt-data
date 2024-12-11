def check_type(tup):
    return len(set(type(x) for x in tup)) == 1
