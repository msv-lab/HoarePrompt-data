#State of the program right berfore the function call: start and end are integers where start <= end, and they represent the range of folder names to be processed. The current directory contains subfolders, some of which may contain .html files.
def func():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        
        arr = input()
        
        count_ones = arr.count('1')
        
        if count_ones == 0:
            results.append('yes')
        elif count_ones % 2 != 0:
            results.append('no')
        elif count_ones == 2:
            if '11' in arr:
                results.append('no')
            else:
                results.append('yes')
        else:
            results.append('yes')
        
    #State: `start` and `end` are integers where `start` <= `end`, `t` is an integer representing the total number of iterations, `results` is a list containing `t` elements. Each element in `results` is determined based on the input `arr` for each iteration: if `arr` contains no '1's, the element is 'yes'; if `arr` contains an odd number of '1's, the element is 'no'; if `arr` contains exactly two '1's and the substring '11' is present, the element is 'no'; otherwise, if `arr` contains exactly two '1's but the substring '11' is not present, the element is 'yes'; if `arr` contains an even number of '1's greater than 2, the element is 'yes'.
    for r in results:
        print(r)
        
    #State: `results` is a list containing `t` elements, and each element in `results` has been printed.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads another integer `n` and a string `arr` consisting of '0's and '1's. It then evaluates `arr` and appends 'yes' or 'no' to a list `results` based on the following rules: if `arr` contains no '1's, the result is 'yes'; if `arr` contains an odd number of '1's, the result is 'no'; if `arr` contains exactly two '1's and the substring '11' is present, the result is 'no'; otherwise, the result is 'yes'. Finally, it prints each element in `results`. The function does not process subfolders or handle `.html` files as mentioned in the annotations.

