#State of the program right berfore the function call: a, b, and c are positive integers representing the number of lemons, apples, and pears respectively, with values in the range 1 ≤ a, b, c ≤ 1000.
def func():
    a = int(input())
    b = int(input())
    c = int(input())
    min_lemon = min(a, b // 2, c // 4)
    print(min_lemon + min_lemon * 2 + min_lemon * 4)
#Overall this is what the function does:The function accepts three positive integer inputs representing the number of lemons, apples, and pears. It computes the minimum number of complete sets that can be formed using these fruits, where each set consists of 1 lemon, 2 apples, and 4 pears, and then calculates the total number of fruits in those sets. The function prints the result, which is the minimum number of complete sets multiplied by 7 (1 lemon + 2 apples + 4 pears per set). Note that the function does not return any value; it only prints the output.

