#State of the program right berfore the function call: # Precondition
**a and b are non-negative integers represented as strings with at most 10^6 digits.**
def func_1():
    data = input().split()
    a = data[0].lstrip('0')
    b = data[1].lstrip('0')
    if (not a) :
        a = '0'
    #State of the program after the if block has been executed: *a is a non-negative integer represented as a string with at most 10^6 digits. If a is false (0 as a string), b is assigned the value of the string at index 1 of the list data after removing leading zeros.
    if (not b) :
        b = '0'
    #State of the program after the if block has been executed: *a is a non-negative integer represented as a string with at most 10^6 digits. If a is false (0 as a string), b is assigned the value of the string at index 1 of the list data after removing leading zeros. The current value of b is false (0).
    if (len(a) < len(b)) :
        print('<')
    else :
        if (len(a) > len(b)) :
            print('>')
        else :
            if (a < b) :
                print('<')
            else :
                if (a > b) :
                    print('>')
                else :
                    print('=')
                #State of the program after the if-else block has been executed: *a is a non-negative integer represented as a string with at most 10^6 digits. If a > b, b is assigned the value of the string at index 1 of the list data after removing leading zeros if a is false (0 as a string) or b was already assigned a value. The length of a is greater than or equal to the length of b and the length of a is less than or equal to the length of b. The condition (a < b) is false, indicating that a is greater than or equal to b. If a is not greater than b, then b is assigned the value 0.
            #State of the program after the if-else block has been executed: *a is a non-negative integer represented as a string with at most 10^6 digits. If a is less than b, b is assigned the value of the string at index 1 of the list data after removing leading zeros if a is false or b was already assigned a value. The length of a is greater than or equal to the length of b and the length of a is less than or equal to the length of b. The condition (a < b) is true, indicating that a is less than b. Therefore, the output is '<'. If a is not less than b, then a is greater than or equal to b and b is assigned the value of the string at index 1 of the list data after removing leading zeros if a is false or b was already assigned a value.
        #State of the program after the if-else block has been executed: *a is a non-negative integer represented as a string with at most 10^6 digits. If the length of a is greater than the length of b, b is updated according to specific criteria. If a is less than b, b is updated to a specific value based on the conditions provided. The length of a is greater than or equal to the length of b in all scenarios, and the final state of the program varies based on the relationship between a and b.
    #State of the program after the if-else block has been executed: *`a` is a non-negative integer represented as a string with at most 10^6 digits. If the length of `a` is less than the length of `b`, then `b` is assigned the value of the string at index 1 of the list data after removing leading zeros. If the length of `a` is greater than or equal to the length of `b`, the final state of the program depends on the relationship between `a` and `b`, with `b` being updated based on specific criteria related to the comparison of `a` and `b`.
#Overall this is what the function does:The function takes two non-negative integers represented as strings with at most 10^6 digits, compares them, and prints whether the first integer is less than, equal to, or greater than the second integer. The function handles cases where the input strings contain leading zeros by removing them. The code does not explicitly return any value, but it prints the result of the comparison.

