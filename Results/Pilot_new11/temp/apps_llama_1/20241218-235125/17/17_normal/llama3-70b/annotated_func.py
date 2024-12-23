#State of the program right berfore the function call: The function func takes no arguments, and the inputs are given in the problem description as four non-negative integers cnt_1, cnt_2, cnt_3, and cnt_4, each representing the number of strings of a specific type, read from the input in the given order.
def func():
    cnt1, cnt2, cnt3, cnt4 = map(int, [input() for _ in range(4)])
    if (cnt3 > cnt1) :
        print(0)
    else :
        print(1)
    #State of the program after the if-else block has been executed: `cnt1`, `cnt2`, `cnt3`, `cnt4` are non-negative integers. If `cnt3` is higher than `cnt1`, the value 0 has been printed. If `cnt3` is less than or equal to `cnt1`, the value 1 has been printed to the console.
#Overall this is what the function does:The function reads four non-negative integers from the input, representing the counts of different string types, and prints 0 if the count of the third type is greater than the count of the first type; otherwise, it prints 1. The function does not perform any validation on the input values beyond assuming they are non-negative integers, and it does not utilize the counts of the second and fourth string types. The final state of the program after execution is that one of two values (0 or 1) has been printed to the console based on the comparison between the first and third input counts, and the input values are stored in variables within the function's scope but are not returned or further processed.

