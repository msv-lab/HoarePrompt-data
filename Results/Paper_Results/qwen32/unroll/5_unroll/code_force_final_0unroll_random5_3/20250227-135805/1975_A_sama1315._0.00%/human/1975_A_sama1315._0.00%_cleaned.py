def func_1(arr):
    if all((arr[i] <= arr[i + 1] for i in range(len(arr) - 1))):
        return 'Yes'
    return 'No' if any((arr[i] > arr[i + 1] for i in range(len(arr) - 1))) else 'Yes'

def func_2():
    import sys
    input = sys.stdin.read
    data = input().split()
    index = 0
    t = int(data[index])
    index += 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        result = func_1(arr)
        results.append(result)
    print('\n'.join(results))
if __name__ == '__main__':
    func_2()