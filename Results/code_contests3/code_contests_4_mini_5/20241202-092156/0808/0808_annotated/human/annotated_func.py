#State of the program right berfore the function call: Each dataset consists of an integer n (1 ≤ n ≤ 999,999), and there are at most 30 datasets provided.
def func():
    a = [True] * 1000000
    for i in range(2, 1000000):
        if a[i - 1]:
            for j in range(i ** 2 - 1, 1000000, i):
                a[j] = False
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where all elements that are not prime indices are False, and all prime indexed elements are True (starting index is 0).
    for s in sys.stdin:
        print(a[1:int(s)].count(True))
        
    #State of the program after the  for loop has been executed: `a` is a list of 1,000,000 elements where all non-prime indices are False and all prime indexed elements are True; the count of True elements in the slice `a[1:int(s)]` is printed for each input read from `sys.stdin`.
#Overall this is what the function does:The function processes up to 30 datasets of integers (each ranging from 1 to 999,999) and prints the count of prime numbers up to each input integer. It does not handle invalid inputs or return values.

