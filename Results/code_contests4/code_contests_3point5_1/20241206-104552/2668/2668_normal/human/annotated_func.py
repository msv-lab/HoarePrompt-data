#State of the program right berfore the function call: **Precondition**: **num is a positive integer, lis1 is a list of positive integers with length n, low and high are positive integers such that low <= high <= 10^9.**
def func_1(num, lis1, low, high):
    while low <= high:
        midone = low + (high - low) / 2
        
        if num == lis1[midone][0]:
            return True, lis1[midone][1]
        elif num > lis1[midone][0]:
            low = midone + 1
        else:
            high = midone - 1
        
    #State of the program after the loop has been executed: If the loop executes until the end, it means no match was found and the loop terminated when low was greater than high. Thus, the output state would be that the program returns False, indicating that the number 'num' was not found in 'lis1'.
    return False, -1
    #The program returns False, indicating that the number 'num' was not found in 'lis1'.
#Overall this is what the function does:The function `func_1` accepts four parameters: `num`, `lis1`, `low`, and `high`. It performs a binary search on the list `lis1` to find the value of `num`. If the value is found, it returns True along with the corresponding value at index 1 of the list `lis1`. If `num` is not found, it returns False along with -1. The function handles the edge cases of the loop terminating without finding a match by returning False and -1.

#State of the program right berfore the function call: **
def func_2():
    if os.path.exists('input.txt') :
        input = open('input.txt', 'r')
    else :
        input = sys.stdin
    #State of the program after the if-else block has been executed: *If 'input.txt' exists, the file is opened in read mode. Otherwise, if 'input.txt' does not exist, `input` is assigned `sys.stdin`.
    n = int(input.readline())
    init = list(map(int, input.readline().split()))
    init = sorted(init, reverse=True)
    counts = [(1, init[0])]
    for (i, x) in enumerate(init):
        if i == 0:
            continue
        
        if init[i] == init[i - 1]:
            counts.append((counts[len(counts) - 1][0] + 1, init[i]))
        else:
            counts.append((1, init[i]))
        
    #State of the program after the  for loop has been executed: `n` is an integer read from the input source, `init` is a sorted list in descending order with at least 1 element, `counts` is a list containing tuples representing the counts of consecutive elements in `init`, `i` is the index of the last element processed in the `init` list, `x` is the last element in the `init` list. If the loop does not execute, `counts` will contain a single tuple (1, largest element of `init`).
    uniques = []
    for (i, x) in enumerate(counts):
        if i + 1 == len(counts):
            uniques.append(counts[i])
            break
        
        if counts[i][1] != counts[i + 1][1]:
            uniques.append(counts[i])
        
    #State of the program after the  for loop has been executed: `n` is an integer, `init` is a sorted list in descending order with at least 1 element, `counts` is a list containing tuples representing the counts of consecutive elements in `init`, `i` is the index of the last tuple in `counts` before the loop exits, `x` is the last element of that tuple, `uniques` contains all unique tuples from `counts` where the count value changes.
    uniques = sorted(uniques, reverse=True)
    m = int(input.readline())
    audio = list(map(int, input.readline().split()))
    subs = list(map(int, input.readline().split()))
    res, anss = False, 0
    audio = [(audio[i], i + 1) for i in range(len(audio))]
    audio2 = sorted(audio)
    for i in range(len(uniques)):
        back = func_1(uniques[i][1], audio2, 0, len(audio2) - 1)
        
        if back[0]:
            res = True
            anss = back
            templis = []
            for y in xrange(len(subs)):
                if audio[y][0] == uniques[i][1]:
                    templis.append((subs[y], y + 1))
            for z in range(len(uniques)):
                back = func_1(uniques[z][1], templis, 0, len(templis) - 1)
                if back[0]:
                    res = True
                    anss = back
                    break
            break
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, the final values of `uniques[i][1]`, `audio2`, `anss`, `templis`, `subs`, `y`, `uniques`, `z`, `back`, `res`, `i` are in their respective states. The loop will break out with the final value of `anss`.
    if (res == False) :
        subs = [(subs[i], i + 1) for i in range(len(subs))]
        subs = sorted(subs)
        for i in range(len(uniques)):
            back = func_1(uniques[i][1], subs, 0, len(subs) - 1)
            
            if back[0]:
                res = True
                anss = back
                break
            
        #State of the program after the  for loop has been executed: After the loop executes, `uniques[i][1]`, `audio2`, `anss`, `templis`, `subs` are still sorted in ascending order. `y`, `uniques`, `z`, `back` are assigned the return value of `func_1`. `res` is True if at least one `back[0]` is True, otherwise False. `i` is the index of the last iteration. `anss` is assigned the value of `back` from the last iteration where `back[0]` is True.
    #State of the program after the if block has been executed: *After the loop finishes executing, the final values of `uniques[i][1]`, `audio2`, `anss`, `templis`, `subs` are still sorted in ascending order. `y`, `uniques`, `z`, `back` are assigned the return value of `func_1`. `res` is True if at least one `back[0]` is True, otherwise False. `i` is the index of the last iteration. The final value of `anss` is assigned the value of `back` from the last iteration where `back[0]` is True.
    if res :
        output = anss[1]
    else :
        output = 1
    #State of the program after the if-else block has been executed: *After the if-else block executes, the variables maintain their ascending order. `uniques[i][1]`, `audio2`, `anss`, `templis`, `subs` are sorted in ascending order. `y`, `uniques`, `z`, `back` are assigned the return value of `func_1`. `res` is True if at least one `back[0]` is True, otherwise False. `i` is the index of the last iteration. If `res` is True, `output` is assigned the value of `anss[1]` from the last iteration where `back[0]` is True. If `res` is False, `output` is assigned the value 1.
    if os.path.exists('output.txt') :
        open('output.txt', 'w').writelines(str(output))
    else :
        sys.stdout.write(str(output))
    #State of the program after the if-else block has been executed: *After the if-else block executes, the variables maintain their ascending order. `uniques[i][1]`, `audio2`, `anss`, `templis`, `subs` are sorted in ascending order. `y`, `uniques`, `z`, `back` are assigned the return value of `func_1`. `res` is True if at least one `back[0]` is True, otherwise False. `i` is the index of the last iteration. If `res` is True, `output` is assigned the value of `anss[1]` from the last iteration where `back[0]` is True. If `res` is False, `output` is assigned the value 1. Additionally, if 'output.txt' exists, the content is updated with the new value of `output`. If 'output.txt' does not exist, the output is written to the standard output using `sys.stdout.write(str(output))`.
#Overall this is what the function does:The function does not accept any parameters and performs a series of operations on input data read from either a file or standard input. It processes the data to find unique elements and perform certain calculations. Eventually, it writes the output to a file 'output.txt' if it exists; otherwise, it writes to the standard output.

