def left_rotate(n, d):
    d = d % 32  # to handle cases where d is greater than 32
    return (n << d) | (n >> (32 - d))
