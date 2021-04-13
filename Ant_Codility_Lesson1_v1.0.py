# ------------------------------------------------
# Program by Tony Push
# 
#
# Version      Date        Info
# 1.0          2021        Task 1
#
# ------------------------------------------------
## Task description
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
# Write a function:
# def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.
# Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
#
#Write an efficient algorithm for the following assumptions: N is an integer within the range [1..2,147,483,647].
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------

import sys
X_Number = input("Input N =")
print(X_Number)
N = int(X_Number)

if (N < 1) or (N > 2147483647):
    sys.exit("N is out of range.")
    
Binar = str(bin(N))[2:]
Binar_group = False
Binar_highest = 0
Binar_zero_counter = 0
print(Binar)

for char in Binar:
    if char == '1':
        if Binar_highest < Binar_zero_counter:
            Binar_highest = Binar_zero_counter
        Binar_group = True
        Binar_zero_counter = 0
    elif Binar_group:
        Binar_zero_counter += 1
print(Binar_highest)