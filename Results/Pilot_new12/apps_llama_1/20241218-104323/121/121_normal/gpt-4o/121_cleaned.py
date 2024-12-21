def func_1():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    s = data[1]
    if n % 4 != 0:
        print('===')
        return
    target_count = n // 4
    counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for char in s:
        if char in counts:
            counts[char] += 1
    for char in counts:
        if counts[char] > target_count:
            print('===')
            return
    result = list(s)
    for i in range(n):
        if result[i] == '?':
            for char in counts:
                if counts[char] < target_count:
                    result[i] = char
                    counts[char] += 1
                    break
    print(''.join(result))
func_1()