# write your code here
favorite_animals = ['dog', 'cat', 'monkey','rabbit']
print(favorite_animals)
print(f'the second element in the list is {favorite_animals[1]}')
favorite_animals.pop(2)

favorite_animals.append('tiger')
for animal in favorite_animals:
    print('i love',animal)

numbers = [1, 2, 3, 4, 5]
numbers_sum = 0

for num in numbers:
    numbers_sum = (num + numbers_sum)
    print(numbers_sum)