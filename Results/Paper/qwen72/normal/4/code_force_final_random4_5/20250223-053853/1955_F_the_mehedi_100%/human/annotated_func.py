#State of the program right berfore the function call: The function `func` is expected to take four integers as input, representing the counts of 1s, 2s, 3s, and 4s in the sequence, respectively. These integers are non-negative and do not exceed 200.
def func():
    for _ in range(int(input())):
        a = list(map(int, input().split()))
        
        cnt = 0
        
        if a[0] % 2 == a[1] % 2 == a[2] % 2 == 1:
            cnt += 1
        
        for x in a:
            cnt += math.floor(x / 2)
        
        print(cnt)
        
    #State: The function `func` will print the value of `cnt` for each iteration of the loop, where `cnt` is calculated based on the input list `a` and the condition specified. The variables `a` and `cnt` will be re-initialized in each iteration, and their final values after the loop will be the values from the last iteration. The input list `a` will contain four integers, and `cnt` will be the sum of the floor division of each element in `a` by 2, plus 1 if all elements in `a` are odd.
#Overall this is what the function does:The function `func` reads an integer from the user input to determine the number of iterations. For each iteration, it reads four integers from the user input, representing counts of 1s, 2s, 3s, and 4s. It calculates a value `cnt` based on these counts: if all four counts are odd, `cnt` is incremented by 1, and for each count, `cnt` is incremented by the floor division of the count by 2. The function prints the value of `cnt` for each iteration. After the loop, the variables `a` and `cnt` will retain the values from the last iteration, but these are not returned or used outside the function. The function does not return any value.

