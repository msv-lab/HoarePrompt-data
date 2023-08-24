# Question: 0757
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
Vasya has got many devices that work on electricity. He's got n supply-line filters to plug the devices, the i-th supply-line filter has a_{i} sockets.

Overall Vasya has got m devices and k electrical sockets in his flat, he can plug the devices or supply-line filters directly. Of course, he can plug the supply-line filter to any other supply-line filter. The device (or the supply-line filter) is considered plugged to electricity if it is either plugged to one of k electrical sockets, or if it is plugged to some supply-line filter that is in turn plugged to electricity. 

What minimum number of supply-line filters from the given set will Vasya need to plug all the devices he has to electricity? Note that all devices and supply-line filters take one socket for plugging and that he can use one socket to plug either one device or one supply-line filter.


-----Input-----

The first line contains three integers n, m, k (1 ≤ n, m, k ≤ 50) — the number of supply-line filters, the number of devices and the number of sockets that he can plug to directly, correspondingly. The second line contains n space-separated integers a_1, a_2, ..., a_{n} (1 ≤ a_{i} ≤ 50) — number a_{i} stands for the number of sockets on the i-th supply-line filter.


-----Output-----

Print a single number — the minimum number of supply-line filters that is needed to plug all the devices to electricity. If it is impossible to plug all the devices even using all the supply-line filters, print -1.


-----Examples-----
Input
3 5 3
3 1 2

Output
1

Input
4 7 2
3 3 2 4

Output
2

Input
5 5 1
1 3 1 2 1

Output
-1



-----Note-----

In the first test case he can plug the first supply-line filter directly to electricity. After he plug it, he get 5 (3 on the supply-line filter and 2 remaining sockets for direct plugging) available sockets to plug. Thus, one filter is enough to plug 5 devices.

One of the optimal ways in the second test sample is to plug the second supply-line filter directly and plug the fourth supply-line filter to one of the sockets in the second supply-line filter. Thus, he gets exactly 7 sockets, available to plug: one to plug to the electricity directly, 2 on the second supply-line filter, 4 on the fourth supply-line filter. There's no way he can plug 7 devices if he use one supply-line filter.
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
n, m, k = map(int, input().split())
filters = list(map(int, input().split()))

filters.sort(reverse=True)  # sort filters in descending order

sockets = k  # number of available sockets
filters_needed = 0  # number of filters needed
i = 0  # index for iterating through filters

# iterate through filters and check if devices can be plugged
while i < n and sockets < m:
    sockets += filters[i] - 1  # add sockets from filter
    filters_needed += 1  # increment number of filters needed
    i += 1

if sockets < m:
    print(-1)  # not enough sockets for all devices
else:
    print(filters_needed)  # minimum number of filters needed
#@!CODE END!@#
````

---

