alphabets = "abcdefghijklmnopqrstuvwxyz"
 
def solve():
    n, k, m = map(int,input().split())
    string = input().strip()
    block = set()
    possible_missing_subseq = []
    
    for s in string:
        block.add(s)
        if len(block) == k:
            possible_missing_subseq.append(s)
            block.clear()
            
    if len(possible_missing_subseq) == n:
        print("yes")
    else:
        print("no")
        for char in alphabets:
            if char not in block:
                while len(possible_missing_subseq) < n:
                    possible_missing_subseq.append(char)
                break
        print("".join(possible_missing_subseq))
 
 
t = int(input())
for _ in range(t):
    solve()