Is the given Python program correct based on the problem description and the correct execution states of the program provided as comment?



# Problem:
Given 5 non empty lists representing:
the number of first-semester students per class at Building A 
the number of administarators per class at Building A 
the number of first-semester students per class at Building B
the number of administarators per class at Building B
the number of professors per class at building B
there are 12 classes at building A and 16 at building B
Make the building have equal number of people by removing the extra people from the more populous building.
Calculate a equal bonus for each moved person. The bonus pool is created by every staying person at both buildings contributing $10.
return the bonus that was given at each mover


# Annotated Program:

#State of the program right berfore the function call: students_A and admins_A are lists of 12 non-negative integers representing the number of first-semester students and administrators per class at Building A, respectively. students_B, admins_B and profs_B are lists of 16 non-negative integers representing the number of first-semester students and administrators per class at Building B, respectively.
def func_1(students_A, admins_A, students_B, admins_B, profs_B):
    total_A = sum(students_A) + sum(admins_A)
    total_B = sum(students_B) + sum(admins_B) +sum(profs_B)
    surplus = abs(total_A - total_B)
    stayers = total_A + total_B - surplus
    bonus_pool = stayers * 10
    bonus_per_moved = bonus_pool / surplus
    return bonus_per_moved
    #The program returns `bonus_per_moved` which is `bonus_pool / surplus`. Given that 'total_A' is a positive integer equal to the number of people originally at building A, and 'total_B' is a positive integer equal to the number of people originally at building B,  `bonus_pool` is a positive integer equal to `20 * min(total_A, total_B)` and `surplus` is a positive integer or 0 equal to the  absolute difference between `total_A` and `total_B`, the program returns `(20 * min(total_A, total_B)) / abs(total_A - total_B)`.

Reply Correctness: **True**  if the given program is correct or Correctness: **False**  if the given program is incorrect.