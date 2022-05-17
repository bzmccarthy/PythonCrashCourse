for value in range(1,5):
    print(value)
    
for value in range(6):
    print(value)
    
numbers = list(range(1,6))

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []

for i in range(1,11):
    temp = i ** 2
    squares.append(temp)
    
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))