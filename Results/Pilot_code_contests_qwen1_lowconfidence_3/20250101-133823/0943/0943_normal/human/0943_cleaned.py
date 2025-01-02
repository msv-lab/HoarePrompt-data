def func_1(i):
    return 2 * i + 1

def func_2(i):
    return 2 * i + 2

def func_3(i):
    return int((i - 1) / 2)

def func_4(array, i, item_num):
    left = func_1(i)
    right = func_2(i)
    largest = i
    if left < item_num and array[left] > array[largest]:
        largest = left
    if right < item_num and array[right] > array[largest]:
        largest = right
    if largest != i:
        tmp = array[i]
        array[i] = array[largest]
        array[largest] = tmp
        func_4(array, largest, item_num)

def func_5():
    size = int(sys.stdin.readline().strip())
    array = map(lambda x: int(x), sys.stdin.readline().strip().split(' '))
    for i in reversed(range(0, func_3(size))):
        func_4(array, i, size)
if __name__ == '__main__':
    func_5()