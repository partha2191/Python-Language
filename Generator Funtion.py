# Python Keyword
import keyword
print(keyword.kwlist)

# Normal Function
def fun():
  s = 0;
  for i in range(10):
    s+=i
  return s

print(fun())

# Generator Function
def fun1():
  s = 0
  for i in range(10):
    s += i
    yield s

for i in fun1():
  print(i)

# Print every next element return by generator function
list = fun1()
print(next(list))