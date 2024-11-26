if __name__ == '__main__':
    n = int(raw_input().strip())
    digits = map(int, raw_input().strip())
    if sum(digits[:n / 2]) == sum(digits[n / 2 + n % 2:]):
        print('YES')
    else:
        print('NO')