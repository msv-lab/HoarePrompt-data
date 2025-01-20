input = sys.stdin.read

def func_1(A):
    (a, b, c, d) = (A[0][0], A[0][1], A[1][0], A[1][1])
    det = a * d - b * c
    if det == 0:
        return 0.0
    if abs(a) >= max(abs(b), abs(c), abs(d)):
        a_prime = b * c / d if d != 0 else 0
        min_norm_value = abs(a - a_prime)
    elif abs(b) >= max(abs(a), abs(c), abs(d)):
        b_prime = a * d / c if c != 0 else 0
        min_norm_value = abs(b - b_prime)
    elif abs(c) >= max(abs(a), abs(b), abs(d)):
        c_prime = a * d / b if b != 0 else 0
        min_norm_value = abs(c - c_prime)
    else:
        d_prime = b * c / a if a != 0 else 0
        min_norm_value = abs(d - d_prime)
    return min_norm_value

def func_2():
    data = input().split()
    (a, b) = (int(data[0]), int(data[1]))
    (c, d) = (int(data[2]), int(data[3]))
    A = [[a, b], [c, d]]
    result = func_1(A)
    print(f'{result:.10f}')
if __name__ == '__main__':
    func_2()