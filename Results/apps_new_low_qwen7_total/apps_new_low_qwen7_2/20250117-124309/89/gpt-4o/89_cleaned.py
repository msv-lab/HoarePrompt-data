def func_1(a, b):

    def has_exactly_one_zero_in_binary(x):
        binary_representation = bin(x)[2:]
        return binary_representation.count('0') == 1
    count = 0
    for year in range(a, b + 1):
        if has_exactly_one_zero_in_binary(year):
            count += 1
    return count
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    a = int(data[0])
    b = int(data[1])
    result = func_1(a, b)
    print(result)