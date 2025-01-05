#State of the program right berfore the function call: n is an even integer greater than or equal to 2. v_1, v_2, ..., v_n are integers such that 1 <= v_i <= 10^5 for i = 1, 2, ..., n.**
def func():
    n = int(raw_input())
    v = map(int, raw_input().split())
    even = [vi for i, vi in enumerate(v) if i % 2 == 0]
    odd = [vi for i, vi in enumerate(v) if i % 2 == 1]
    evenc = collections.Counter(even)
    oddc = collections.Counter(odd)
    evenc_most_common = evenc.most_common(len(set(even))) + [(None, 0)]
    oddc_most_common = oddc.most_common(len(set(odd))) + [(None, 0)]
    m = []
    for i in range(2):
        for j in range(2):
            if evenc_most_common[i][0] != oddc_most_common[j][0]:
                a = len(even) - evenc_most_common[i][1]
                b = len(odd) - oddc_most_common[j][1]
                m.append(a + b)
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `m` contains the result of `a + b` appended at the end for each iteration where `evenc_most_common[i][0] != oddc_most_common[j][0]`. If the condition `evenc_most_common[i][0] != oddc_most_common[j][0]` is false for all iterations, then `m` remains the same as the initial state.
    print(min(m))
#Overall this is what the function does:The function reads an integer n and a list of integers v. It then separates the elements of v into even and odd indexed lists, counts the occurrences of each value in the lists, finds the most common values in each list, and calculates the difference between the total number of elements and the frequency of the most common values. Finally, it prints the minimum sum of these differences.

