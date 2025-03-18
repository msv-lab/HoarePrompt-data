def func_1(n, operations, queries):
    array = []
    result = []
    for (op_type, value) in operations:
        if op_type == 1:
            array.append(value)
        else:
            array.extend([array[i] for i in range(len(array))])
    for k in queries:
        result.append(array[(k - 1) % len(array)])
    return result

def func_2():
    t = int(input())
    for _ in range(t):
        (n, q) = map(int, input().split())
        operations = [list(map(int, input().split())) for _ in range(n)]
        queries = list(map(int, input().split()))
        result = func_1(n, operations, queries)
        print(*result)
if __name__ == '__main__':
    func_2()