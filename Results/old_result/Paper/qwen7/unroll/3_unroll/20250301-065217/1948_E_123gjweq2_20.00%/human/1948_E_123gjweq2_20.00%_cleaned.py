def func_1(n, k):
    cliques = ceil(n / k)
    arr = [0] * n
    cliquess = [0] * n

    def make_array(left, right, clique):
        small_element = left + 1
        big_element = right + 1
        mid = (big_element - small_element) // 2
        not_mid = right - left + 1 - mid
        for i in range(mid):
            arr[left + i] = small_element + i
            cliquess[left + i] = clique
        for i in range(not_mid):
            arr[left + mid + i] = big_element - i
            cliquess[left + mid + i] = clique
    for i in range(cliques):
        make_array(i * k, min((i + 1) * k - 1, n - 1), i + 1)
    print(*arr)
    print(cliques)
    print(*cliquess)
testcases = range(int(input()))
for case in testcases:
    (n, k) = [int(i) for i in input().split(' ')]
    func_1(n, k)