def tuple_str_int(s):
    return tuple(int(x) for x in s.strip("()").split(","))
