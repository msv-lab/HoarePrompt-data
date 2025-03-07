def func_1(array):
    array.sort()
    beauty = 0
    for i in range(1, len(array)):
        beauty += abs(array[i] - array[i - 1])
    return beauty

def func_2():
    import sys
    input = sys.stdin.read
    data = input().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        array = list(map(int, data[index:index + n]))
        index += n
        result = func_1(array)
        results.append(result)
    for result in results:
        print(result)
if __name__ == '__main__':
    func_2()