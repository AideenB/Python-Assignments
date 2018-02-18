# Aideen Byrne 17/02/2018 sunday
#Project Euler Archived Problem 2 - sum of even valued terms of Fibonacci sequence to 4 million

i = 0
j = 1

while n >= 0:
    i, j = j, i + j
    n = n - 1

print(i)