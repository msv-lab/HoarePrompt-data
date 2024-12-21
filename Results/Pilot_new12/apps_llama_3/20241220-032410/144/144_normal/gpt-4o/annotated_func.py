#State of the program right berfore the function call: The input is an array of n positive integers, where n is a positive integer such that 1 <= n <= 100 000, and each integer in the array is between 1 and 10^9 (inclusive).
def func():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = 1
    for num in a:
        if num >= mex:
            mex += 1
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 1 and 100,000 (inclusive), `a` is a sorted list of `n` positive integers between 1 and 10^9 (inclusive), `num` is the last element in the list `a`, and `mex` is the smallest positive integer that is not in the list `a` or is greater than the maximum value in `a` if all smaller positive integers are present in `a`.
    print(mex)
#Overall this is what the function does:The function accepts a positive integer `n` and an array of `n` positive integers as input, sorts the array in ascending order, and finds the smallest positive integer (MEX) that is not present in the array. The MEX is then printed as output. The function processes the input array based on the following conditions: it iterates through the sorted array and increments the MEX value until it finds a number in the array that is greater than or equal to the current MEX value. The function handles edge cases, including arrays with duplicate numbers, arrays with numbers greater than the MEX value, and arrays with all numbers from 1 to `n` present. The function does not modify the original input array beyond sorting it. After execution, the program's state reflects the input array being sorted and the MEX value being printed, with the original input array's contents modified to be sorted. The function does not handle cases where the input array is empty or `n` is not a positive integer, as these cases are not specified in the code. However, based on the code provided, it is assumed that the input will always be valid.

