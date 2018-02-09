#Aideen Byrne 06-02-2018
#Collatz Conjecture - https://en.wikipedia.org/wiki/Collatz_conjecture 
#with help from https://www.webucator.com/blog/2015/07/collatz-conjecture-in-python/

num = 17
 
while num != 1:
    print(num)
    if num % 2 == 0:
      num = int(num / 2)
    else:
      num = int(3 * num + 1)
else:
    print(num)
