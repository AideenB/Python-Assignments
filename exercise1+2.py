# Code by Ian McLoughlin
# A program that displays Fibonacci numbers using people's names.
# My surname is Byrne The first letter B is number 66 The last letter e is number 101 Fibonacci number 167 is 35600075545958458963222876581316753used in a string returns an integer representing the Unicode code point of a character e.g. ord (' a ') returns the integer 97.
# My name is Aideen, so the first and last letter of my name (A + N = 1 + 14) give the number 15.  The 15th Fibonacci number is 610.


def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Byrne"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)