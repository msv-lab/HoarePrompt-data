def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    MOD = 10 ** 9 + 7
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        (n, k) = (int(data[index]), int(data[index + 1]))
        index += 2
        a = list(map(int, data[index:index + n]))
        index += n
        initial_sum = sum(a) % MOD

        def kadane(arr):
            max_ending_here = max_so_far = arr[0]
            for x in arr[1:]:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        max_subarray_sum = kadane(a)
        if max_subarray_sum > 0:
            result = (initial_sum + k * max_subarray_sum) % MOD
        else:
            result = initial_sum % MOD
        results.append(result)
    for result in results:
        print(result)
if __name__ == '__main__':
    func_1()