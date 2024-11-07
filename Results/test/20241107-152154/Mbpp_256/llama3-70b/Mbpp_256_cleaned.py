def func_1(n: int) -> int:
    def func_2(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    for num in range(2, n):
        if func_2(num):
            count += 1
    return count