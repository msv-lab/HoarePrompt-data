def remove_nested(tup):
    return tuple(x for x in tup if not isinstance(x, tuple))
