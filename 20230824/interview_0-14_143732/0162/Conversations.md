# Question: 0162
## Generation 1
### Conversations

---

**role**: 
````markdown
system
````

---

**content**: 
````markdown
I want you to act as a Coding Contest Participant. Imagine that you are taking part in a prestigious coding competition. Your task is to design an efficient algorithm for a complex problem. You need to consider all possible edge cases, optimize for efficiency, and ensure that your solution is clean and readable. In addition, provide a Python code of your solution, and put the solution in a code delimiter.For example:
### QUESTION
A. Watermelon
time limit per test: 1 second
memory limit per test: 64 megabytes
input: standard input
output: standard output
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 <= w <= 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.

Examples
input
8
output
YES
Note
For example, the boys can divide the watermelon into two parts of 2 and 6 kilos respectively (another variant — two parts of 4 and 4 kilos).

### Expected response from you
#@!CODE START!@#
w = int(input())
if w % 2 == 1 or w < 4:
print("NO")
else:
print("YES")
#@!CODE END!@#
````

---

**role**: 
````markdown
user
````

---

**content**: 
````markdown
### QUESTION
Luba thinks about watering her garden. The garden can be represented as a segment of length k. Luba has got n buckets, the i-th bucket allows her to water some continuous subsegment of garden of length exactly a_{i} each hour. Luba can't water any parts of the garden that were already watered, also she can't water the ground outside the garden.

Luba has to choose one of the buckets in order to water the garden as fast as possible (as mentioned above, each hour she will water some continuous subsegment of length a_{i} if she chooses the i-th bucket). Help her to determine the minimum number of hours she has to spend watering the garden. It is guaranteed that Luba can always choose a bucket so it is possible water the garden.

See the examples for better understanding.


-----Input-----

The first line of input contains two integer numbers n and k (1 ≤ n, k ≤ 100) — the number of buckets and the length of the garden, respectively.

The second line of input contains n integer numbers a_{i} (1 ≤ a_{i} ≤ 100) — the length of the segment that can be watered by the i-th bucket in one hour.

It is guaranteed that there is at least one bucket such that it is possible to water the garden in integer number of hours using only this bucket.


-----Output-----

Print one integer number — the minimum number of hours required to water the garden.


-----Examples-----
Input
3 6
2 3 5

Output
2

Input
6 7
1 2 3 4 5 6

Output
7



-----Note-----

In the first test the best option is to choose the bucket that allows to water the segment of length 3. We can't choose the bucket that allows to water the segment of length 5 because then we can't water the whole garden.

In the second test we can choose only the bucket that allows us to water the segment of length 1.
### Requirements
1. Use Standard Input Format (read inputs with `input()`, write results with `print()`)
2. You will NOT return anything except for the program. 
3. DO NOT WRITE PLANS OR EXPLANATIONS
````

---

**role**: 
````markdown
assistant
````

---

**content**: 
````markdown
#@!CODE START!@#
n, k = map(int, input().split())
buckets = list(map(int, input().split()))

hours = k
for bucket in buckets:
    if k % bucket == 0:
        hours = min(hours, k // bucket)

print(hours)
#@!CODE END!@#
````

---

