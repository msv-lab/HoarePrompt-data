#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\), and \(n\) is the length of the list.
def func_1(arr):
    nums = c.Counter(arr)
    start = 0
    vis = set()
    while nums.get(start, 0):
        vis.add(start)
        
        nums[start] -= 1
        
        if nums.get(start + 1, 0):
            nums[start + 1] -= 1
            start += 1
        else:
            print(start + 1)
            return
        
    #State: The value of `start` is some integer, `vis` is a set containing integers from 0 to the final value of `start`, and `nums` is a dictionary where each key is an integer and its value is less than or equal to 0.
    print(start)
    #This is printed: start (where start is some integer)
#Overall this is what the function does:The function accepts a list of non-negative integers `arr` where each integer \(a_i\) satisfies \(0 \le a_i < n\), and \(n\) is the length of the list. It uses a counter to track the occurrences of each integer in the list. The function then iterates through the list, decrementing the count of the current element and its successor if it exists. If it encounters an element whose count is zero and its successor also has a count of zero, it prints the successor and returns. Otherwise, it continues until it reaches the end of the list, printing the final value of `start`. The function does not return any value but prints the final value of `start` or the successor of `start` if applicable.

