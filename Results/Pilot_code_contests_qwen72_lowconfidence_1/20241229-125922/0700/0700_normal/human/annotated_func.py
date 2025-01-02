#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10000, representing the number of data sets. Each data set contains an integer n (1 ≤ n ≤ 150000) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^6). The sum of n over all data sets does not exceed 150000.
def func():
    for i in range(input()):
        n = input()
        
        l = [int(j) for j in raw_input().split(' ')]
        
        minAr = l[-1]
        
        sm = 0
        
        for j in range(len(l) - 2, -1, -1):
            if l[j] < minAr:
                minAr = l[j]
            elif l[j] > minAr:
                sm += 1
        
        print(sm)
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10000\), `i` is `t-1`, `n` is the last input integer (1 ≤ n ≤ 150000), `l` is a list of `n` integers (1 ≤ a_i ≤ 10^6), `minAr` is the minimum value in the list `l` starting from the second last element to the first element (inclusive), `sm` is the count of elements in the list `l` that are strictly greater than `minAr`, and the value of `sm` is printed for each of the `t` data sets. If any list `l` has fewer than 2 elements, `minAr` remains the last element of `l`, while `sm` remains 0.
#Overall this is what the function does:The function `func` processes multiple data sets, each containing an integer `n` and a list of `n` integers. For each data set, it calculates the number of elements in the list that are strictly greater than the minimum value found from the last element to the first. The result, `sm`, is printed for each data set. If a list has fewer than 2 elements, the function prints 0 for that data set. The function reads inputs from standard input and does not return any values. After the function completes, the state of the program includes the processed data sets and the printed results, but the original input values (`t`, `n`, and `l`) are no longer accessible.

