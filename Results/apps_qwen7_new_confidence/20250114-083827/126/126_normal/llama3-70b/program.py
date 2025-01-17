l1, s1, r1, p1 = map(int, input().split())
l2, s2, r2, p2 = map(int, input().split())
l3, s3, r3, p3 = map(int, input().split())
l4, s4, r4, p4 = map(int, input().split())

if (l1 and p1) or (s1 and p1) or (r1 and p1) or \
   (l2 and p2) or (s2 and p2) or (r2 and p2) or \
   (l3 and p3) or (s3 and p3) or (r3 and p3) or \
   (l4 and p4) or (s4 and p4) or (r4 and p4) or \
   (l1 and p4) or (s1 and p4) or (r1 and p4) or \
   (l2 and p1) or (s2 and p1) or (r2 and p1) or \
   (l3 and p2) or (s3 and p2) or (r3 and p2) or \
   (l4 and p3) or (s4 and p3) or (r4 and p3):
    print("YES")
else:
    print("NO")
