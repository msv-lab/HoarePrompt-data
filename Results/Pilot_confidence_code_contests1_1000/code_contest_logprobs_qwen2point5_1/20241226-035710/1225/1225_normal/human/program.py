import random

def distance(p1, p2):
     return pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)
     
lim=1000
#lim=pow(pow(10,10), 10)

sample_num=1000000
samples=[]

for i in range(sample_num):
#    samples.append([random.uniform(-lim, lim), random.uniform(-lim, lim)])
    samples.append([random.randint(-lim, lim), random.randint(-lim, lim)])

N=int(raw_input())

set_points=[]
point_score=[]

for i in range(N):
    point = map(int,raw_input().split())
    set_points.append(point)
    point_score.append(0)

#print set_points
#print samples

for sample in samples:
    p = 0
    d = distance(set_points[p], sample)
    for i in range(1, N):
        tmp_d = distance(set_points[i], sample)
        if d < tmp_d:
            p = i
            d = tmp_d
    point_score[p] += 1
#    print point_score

for score in point_score:
    print (score + 0.00) / sample_num
