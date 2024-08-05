from true_math import divide as true
from fake_math import divide as fake
result1 = true(69, 3)
result2 = fake(3, 0)
result3 = true(49, 7)
result4 = fake(15, 0)
result5 = true(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)