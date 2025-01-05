#State of the program right berfore the function call: n is an even integer greater than or equal to 2. v_1, v_2, ..., v_n are integers in the range [1, 10^5].**
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
        
    #State of the program after the  for loop has been executed: `oddc_most_common` contains the most common elements from `odd` along with their counts, `m` contains the sum of the differences between the lengths of `even` and the counts of the most common elements in `evenc_most_common` and the lengths of `odd` and the counts of the most common elements in `oddc_most_common` for all possible combinations of `i` and `j` where `i` is less than the length of `evenc_most_common` and `j` is less than 2
    print(min(m))
#Overall this is what the function does:The function `func` reads an even integer `n` followed by a list of integers `v` and processes the list to find the minimum sum of differences between the lengths of even and odd elements that are not the most common elements in their respective categories. The function then prints this minimum sum. However, the function lacks a proper return value, and its purpose seems to be focused on this specific computation without explicitly returning a result.

