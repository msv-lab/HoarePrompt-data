def func_1(n, row1, row2):
    """
    判断机器人是否能够从 (1,1) 到达 (2,n)。
    """
    half_n = n // 2
    for i in range(half_n - 1):
        if row1[2 * i + 1] == '<' and (row2[2 * i] == '<' or row2[2 * i + 2] == '<'):
            return 'No'
    if row1[n - 1] == '<' and row2[n - 2] == '<':
        return 'No'
    return 'Yes'

def func_2():
    """
    读取输入并处理每个测试用例。
    """
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        row1 = input()
        row2 = input()
        results.append(func_1(n, row1, row2))
    print('\n'.join(results))
if __name__ == '__main__':
    func_2()