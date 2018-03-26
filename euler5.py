#Aideen Byrne 20/02/2018
#Project Euler Problem 5: https://projecteuler.net/problem=5 
#Demonstrate the smallest positive number that is evenly divisible by all the numbers from  to 20

i = 2 #all numbers divisible by 1 so start with next integer
for k in (range(11, 21)):#range from 11 to 20
  if i % k > 0: #if no remainder
    for j in range(11, 21): 
      if (i*j) % k == 0: #even numbers only
        i *= j 
        break 
print (i)
  