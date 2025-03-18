def func_1():
    (n, k) = map(int, input().split(' '))
    permutation = [0] * n
    idx = 0
    idx_v = 1
    curr_v = 1
    for i in range(k):
        multiples_of_k_plus_i = i
        while multiples_of_k_plus_i < len(permutation):
            permutation[multiples_of_k_plus_i] = curr_v
            curr_v += 1
            multiples_of_k_plus_i += k
    result = ' '.join([str(v) for v in permutation])
    print(result)

def func_2():
    t = int(input())
    while t > 0:
        func_1()
        t -= 1
if __name__ == '__main__':
    func_2()