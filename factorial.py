#Aideen Byrne 7-3-2018
#Write a Python script containing a function called factorial() that takes a 
#single input/argument which is a positive integer and returns its factorial. 
#The factorial of a number is that number multiplied by all of the positive 
#numbers less than it. For example, the factorial of 5 is 5x4x3x2x1 which equals 
#120. You should, in your script, test the function by calling it with the 
#values 5, 7, and 10.

def factorial(y): #to define function
    if y == 0: #need to make sure not to multiply by O!
        return 1 
    else:
        return y * factorial(y-1) #this ensures y is multiplied by all the numbers less than it (except 0)

print("The factorial of 5 is: ",factorial(5))
print("The factorial of 7 is: ",factorial(7))
print("The factorial of 10 is:",factorial(10))