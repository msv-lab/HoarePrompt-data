def func_1(a, b):
    if (a + b) % 2 == 0:
        return 'Bob'
    else:
        return 'Alice'

def func_2():
    t = int(input('Enter the number of test cases: '))
    results = []
    for _ in range(t):
        (a, b) = map(int, input().strip().split())
        winner = func_1(a, b)
        results.append(winner)
    for result in results:
        print(result)
if __name__ == '__main__':
    func_2()