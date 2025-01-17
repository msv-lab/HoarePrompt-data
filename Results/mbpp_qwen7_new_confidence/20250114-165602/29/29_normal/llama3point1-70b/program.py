def get_equal(tuples):
    length = len(tuples[0])
    for t in tuples:
        if len(t) != length:
            return False
    return True
