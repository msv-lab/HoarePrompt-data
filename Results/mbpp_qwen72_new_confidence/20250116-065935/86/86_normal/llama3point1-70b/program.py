def find_solution(a, b, n):
    def extended_euclidean(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_euclidean(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, y = extended_euclidean(a, b)
    if n % gcd != 0:
        return None
    x *= n // gcd
    y *= n // gcd
    return x, y