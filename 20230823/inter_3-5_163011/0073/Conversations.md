# Question: 0073
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
Mister B once received a gift: it was a book about aliens, which he started read immediately. This book had c pages.

At first day Mister B read v_0 pages, but after that he started to speed up. Every day, starting from the second, he read a pages more than on the previous day (at first day he read v_0 pages, at second — v_0 + a pages, at third — v_0 + 2a pages, and so on). But Mister B is just a human, so he physically wasn't able to read more than v_1 pages per day.

Also, to refresh his memory, every day, starting from the second, Mister B had to reread last l pages he read on the previous day. Mister B finished the book when he read the last page for the first time.

Help Mister B to calculate how many days he needed to finish the book.


-----Input-----

First and only line contains five space-separated integers: c, v_0, v_1, a and l (1 ≤ c ≤ 1000, 0 ≤ l < v_0 ≤ v_1 ≤ 1000, 0 ≤ a ≤ 1000) — the length of the book in pages, the initial reading speed, the maximum reading speed, the acceleration in reading speed and the number of pages for rereading.


-----Output-----

Print one integer — the number of days Mister B needed to finish the book.


-----Examples-----
Input
5 5 10 5 4

Output
1

Input
12 4 12 4 1

Output
3

Input
15 1 100 0 0

Output
15



-----Note-----

In the first sample test the book contains 5 pages, so Mister B read it right at the first day.

In the second sample test at first day Mister B read pages number 1 - 4, at second day — 4 - 11, at third day — 11 - 12 and finished the book.

In third sample test every day Mister B read 1 page of the book, so he finished in 15 days.
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
c, v0, v1, a, l = map(int, input().split())

days = 0
pages_read = 0
current_speed = v0

while pages_read < c:
    days += 1
    pages_read += current_speed

    if current_speed + a <= v1:
        current_speed += a
    else:
        current_speed = v1

    if pages_read >= c:
        break

    pages_read -= l

print(days)
#@!CODE END!@#
````

---

