#Aideen Byrne 06-02-2018
#Collatz Conjecture - https://en.wikipedia.org/wiki/Collatz_conjecture 
#with help from https://www.webucator.com/blog/2015/07/collatz-conjecture-in-python/
#update
num = 17
 
while num != 1: #num not equal to 1
    print(num)
    if num % 2 == 0: #even number
      num = int(num / 2) #if even divide by 2
    else: #if not an even number it must be odd!
      num = int(3 * num + 1) #multiply by 3 and add 1
else:
    print(num)
