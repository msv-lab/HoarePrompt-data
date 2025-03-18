answers = []
numberOfArrays = int(input())
for arrayCounter in range(0, numberOfArrays):
    elementSize = int(input())
    array = list(map(int, input().split()))
    func_3(array)
for ans in answers:
    print(f'{ans}')

def func_1(array, index):
    array[index - 1] = array[index - 1] - 1
    array[index] = array[index] - 2
    array[index + 1] = array[index + 1] - 1
    return array

def func_2(arrayForSuccess):
    for x in arrayForSuccess:
        if x != 0:
            return False
    return True

def func_3(inputarray):
    if func_2(inputarray):
        answers.append('YES')
        return
    loop_counter = 1
    while loop_counter != 100:
        length = len(inputarray)
        highestNumber = -1
        highestIndex = -1
        for elementIndex in range(1, length - 1):
            if inputarray[elementIndex] >= highestNumber:
                highestIndex = elementIndex
                highestNumber = inputarray[elementIndex]
        if highestNumber < 0:
            answers.append('NO')
            return
        newArray = func_1(inputarray, highestIndex)
        if func_2(newArray):
            answers.append('YES')
            return
        loop_counter += 1
    answers.append('NO')

