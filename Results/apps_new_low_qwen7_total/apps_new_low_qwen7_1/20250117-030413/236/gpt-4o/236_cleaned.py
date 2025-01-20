def func_1(n):

    def can_vasya_eat_half(k):
        total = n
        vasya_eaten = 0
        while total > 0:
            if total < k:
                vasya_eaten += total
                total = 0
            else:
                vasya_eaten += k
                total -= k
            total -= total // 10
        return vasya_eaten * 2 >= n
    (left, right) = (1, n)
    while left < right:
        mid = (left + right) // 2
        if can_vasya_eat_half(mid):
            right = mid
        else:
            left = mid + 1
    return left
if __name__ == '__main__':
    n = int(input().strip())
    print(func_1(n))