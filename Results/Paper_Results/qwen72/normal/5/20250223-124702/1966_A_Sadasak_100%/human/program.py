def count_frequencies(arr, k):
    frequency_table = {}
 
    for num in arr:
        frequency_table[num] = frequency_table.get(num, 0) + 1
        if frequency_table[num] > k :
            frequency_table[num] = k
 
    return frequency_table  
 
t = int(input())
for i in range(t):
    n , k = map(int, input().split())
    nums = list(map(int, input().split()))
    if k > n :
        print(n)
    else:
        freq = count_frequencies(nums, k)
        if k in freq.values():
            print(k - 1) 
        else :
            print(n)
 
 
 
 
# t = int(input())
# for i in range(t):
#     n , k = map(int, input().split())
#     if k > n :
#         print(n)
#     elif k == n :
#         print(k - 1)
#     else:
#         nums = list(map(int, input().split()))
#         frequency_table = frequencies_of_frequencies(nums, k)
#         if k in frequency_table and frequency_table[k] > 0:
#             x = 0
#             for num in frequency_table:
#                 if num == k :
#                     continue
#                 x += num * frequency_table[num]
#             print(x)
#         else :
#             print(len(nums))