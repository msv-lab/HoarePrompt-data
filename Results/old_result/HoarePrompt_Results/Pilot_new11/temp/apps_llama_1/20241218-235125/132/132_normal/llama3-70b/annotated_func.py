#State of the program right berfore the function call: The input consists of three lines: the first line contains a positive integer n (1 <= n <= 50) representing the number of piles, the second line contains n non-negative integers x_1, x_2,..., x_n (0 <= x_i <= 1000) representing the number of stones in each pile on the first day, and the third line contains n non-negative integers y_1, y_2,..., y_n (0 <= y_i <= 1000) representing the number of stones in each pile on the second day.
def func():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    if (sum(x) != sum(y)) :
        print('No')
    else :
        x.sort()
        y.sort()
        if (x == y) :
            print('Yes')
        else :
            print('No')
        #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 50, `x` is a sorted list of input integers, `y` is a sorted list of input integers, and the sum of the elements in `x` is equal to the sum of the elements in `y`. If `x` is equal to `y`, 'Yes' has been printed to the console. If `x` is not equal to `y`, 'No' has been printed to the console.
    #State of the program after the if-else block has been executed: *`n` is a positive integer between 1 and 50, `x` is a list of input integers, `y` is a list of input integers. If the sum of `x` is not equal to the sum of `y`, 'No' has been printed. If the sum of `x` is equal to the sum of `y`, then `x` and `y` are sorted lists and either 'Yes' has been printed if `x` is equal to `y`, or 'No' has been printed if `x` is not equal to `y`.
#Overall this is what the function does:The function checks if the distribution of stones in piles on two consecutive days is the same, regardless of the order of the piles. It accepts three lines of input: the number of piles (a positive integer between 1 and 50), the number of stones in each pile on the first day (a list of non-negative integers), and the number of stones in each pile on the second day (a list of non-negative integers). The function returns 'Yes' if the total number of stones and the distribution of stones are the same on both days, and 'No' otherwise. The function performs the following actions: reads the input, checks if the total number of stones is the same on both days, sorts the lists of stones if the total numbers are equal, and compares the sorted lists to determine if the distributions are the same. After the function executes, the program state includes the input variables (number of piles, stones on the first day, and stones on the second day), and the console output ('Yes' or 'No'), with the lists of stones potentially modified to be sorted if the total numbers were equal. The function handles edge cases where the total number of stones is not the same on both days, and where the distributions are the same or different.

