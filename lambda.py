add=lambda a, b: a+b
print(add(10, 20))

nums = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, nums)
print(list(even))

values=[1,2,3,4]
result=(map(lambda x:x+2,values))
print(list(result))

from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda a, b: a + b, nums)
print(result)