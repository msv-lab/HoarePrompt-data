def tuple_to_dict(tup):
    return {tup[i]: tup[i+1] for i in range(0, len(tup), 2)}
