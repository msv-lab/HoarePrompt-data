def minimum_bribes(n, votes):
    limak_votes = votes[0]
    other_votes = votes[1:]
    max_votes = max(other_votes)
    
    if limak_votes > max_votes:
        return 0
    
    bribes = max_votes - limak_votes + 1
    
    return bribes

n = int(input())
votes = list(map(int, input().split()))

bribes_required = minimum_bribes(n, votes)
print(bribes_required)