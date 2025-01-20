(l1, r1, l2, r2, k) = map(int, input().split())
start = max(l1, l2)
end = min(r1, r2)
if start <= k <= end:
    end -= 1
minutes_together = max(0, end - start + 1)
print(minutes_together)