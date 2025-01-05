def func_1(N, NUMBERS):
    n = int(N)
    numbers = [int(s) for s in NUMBERS.split(' ')]
    assert n + 0 == len(numbers) + 1
    sum = 0
    for num in numbers:
        sum += num
    sys.stdout.write(str(int(n * (n + 1) / 2 - sum)) + '\n')
if __name__ == '__main__':
    if True:
        n = raw_input()
        numbers = raw_input()
        func_1(n, numbers)
    else:
        func_1('10', '3 8 10 1 7 9 6 5 2')
    sys.exit(0)