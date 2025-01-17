def index_multiplication(tuple1, tuple2):
    return tuple((a[0]*b[0], a[1]*b[1]) for a, b in zip(tuple1, tuple2))
