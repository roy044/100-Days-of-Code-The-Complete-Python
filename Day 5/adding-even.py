even_sum = 0

for number in range(2, 101, 2):
  even_sum += number
print(even_sum)
  
#or

alternative_sum = 0

for number in range(1, 101):
  if number % 2 == 0:
    # print(number)
    alternative_sum += number
print(alternative_sum)
