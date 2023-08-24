# Question: 0496
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
Petya is preparing for IQ test and he has noticed that there many problems like: you are given a sequence, find the next number. Now Petya can solve only problems with arithmetic or geometric progressions.

Arithmetic progression is a sequence a_1, a_1 + d, a_1 + 2d, ..., a_1 + (n - 1)d, where a_1 and d are any numbers.

Geometric progression is a sequence b_1, b_2 = b_1q, ..., b_{n} = b_{n} - 1q, where b_1 ≠ 0, q ≠ 0, q ≠ 1. 

Help Petya and write a program to determine if the given sequence is arithmetic or geometric. Also it should found the next number. If the sequence is neither arithmetic nor geometric, print 42 (he thinks it is impossible to find better answer). You should also print 42 if the next element of progression is not integer. So answer is always integer.


-----Input-----

The first line contains exactly four integer numbers between 1 and 1000, inclusively.


-----Output-----

Print the required number. If the given sequence is arithmetic progression, print the next progression element. Similarly, if the given sequence is geometric progression, print the next progression element.

Print 42 if the given sequence is not an arithmetic or geometric progression.


-----Examples-----
Input
836 624 412 200

Output
-12

Input
1 334 667 1000

Output
1333



-----Note-----

This problem contains very weak pretests!
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
# Read input sequence
a, b, c, d = map(int, input().split())

# Check if given sequence is arithmetic progression
if b - a == c - b == d - c:
    # Compute the next element in arithmetic progression
    next_element = d + (d - c)
    # Check if next element is an integer
    if next_element % 1 != 0:
        print(42)
    else:
        print(int(next_element))
else:
    # Check if given sequence is geometric progression
    if a != 0 and b != 0 and c != 0 and d != 0:
        if b / a == c / b == d / c:
            # Compute the next element in geometric progression
            next_element = d * (d / c)
            # Check if next element is an integer
            if next_element % 1 != 0:
                print(42)
            else:
                print(int(next_element))
        else:
            print(42)
    else:
        print(42)
#@!CODE END!@#
````

---

