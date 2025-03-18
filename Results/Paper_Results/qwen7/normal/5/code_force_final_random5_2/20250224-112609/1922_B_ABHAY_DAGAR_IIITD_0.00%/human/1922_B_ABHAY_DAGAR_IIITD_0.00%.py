def cnt_cmbnts(test_cases):
    results = []
    
    for _ in range(test_cases):
        n = int(input())
        num_list = list(map(int, input().split()))
        
        num_of_lens = {}
        for x in num_list:
            if x in num_of_lens:
                num_of_lens[x] += 1
            else:
                num_of_lens[x] = 1
 
        res = 0
        total_count = 0
        for cnt in num_of_lens.values():
            if cnt >= 3:
                res += cnt * (cnt - 1) * (cnt - 2) // 6
            if cnt >= 2:
                res += cnt * (cnt - 1) // 2 * total_count
            total_count += cnt
        
        results.append(res)
    
    for result in results:
        print(result)
 
 
t = int(input())
cnt_cmbnts(t)