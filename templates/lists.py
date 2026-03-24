'''num1 = int (input ("Введите число 1: "))
num2 = int (input ("Введите число 2: "))
num3 = int (input ("Введите число 3: "))
num4 = int (input ("Введите число 4: "))
num5 = int (input ("Введите число 5: "))

list = [num1, num2, num3, num4, num5]
length = len[list]
summ = sum(list)

print (f"Список: {list}")
print (length)
print (summ)'''

'''numbers = []
for i in range(5):
numbers = list(range(1, 101))

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
divisible_by_3 = [num for num in numbers if num % 3 == 0]
divisible_by_5 = [num for num in numbers if num % 5 == 0]

print(f"Четные числа: {even_numbers[:10]}...")  # Показываем первые 10
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

print(f"Список: {numbers}")
print(f"Длина списка: {len(numbers)}")
    vowels = "аеёиоуыэюяaeiouAEIOU"
    vowel_words = [word for word in words if word[0] in 
    print(f"Слова, начинающиеся на гласную: {vowel_words}")
'''
print(f"Сумма элементов: {sum(numbers)}")'''

'''numbers_str = input("Введите числа через пробел: ")
numbers = [int(x) for x in numbers_str.split()]

target = int(input("Введите число для поиска: "))

try:
    index = numbers.index(target)
    print(f"Число {target} найдено п    num = int(input(f"Введите число {i+1}: "))
о индексу {index}")
print(f"Нечетные числа: {odd_numbers[:10]}...")
    vowels = "аеёиоуыэюяaeiouAEIOU"
    vowel_words = [word for word in words if word[0] in 
    print(f"Слова, начинающиеся на гласную: {vowel_words}")
'''
except ---ValueError:
    print(f"Число {target} не найдено в списке")'''

print(f"Нечетные числа: {odd_numbers[:10]}...")
    vowels = "аеёиоуыэюяaeiouAEIOU"
numbers = [int(x) for x in numbers_str.split()]
    print(f"Слова, начинающиеся на гласную: {vowel_words}")
'''
'''  
print(f"Нечетные числа: {odd_numbers[:10]}...")
    vowels = "аеёиоуыэюяaeiouAEIOU"
    vowel_words = [word for word in
print(f"Нечетные числа: {odd_numbers[:10]}...")
    vowels = "аеёиоуыэюяaeiouAEIOU"
    vowel_words = [word for word in words if word[0] in 
    print(f"Слова, начинающиеся на гласную: {vowel_words}")
''' words if word[0] in 
    print(f"Слова, начинающиеся на гласную: {vowel_words}")
'''
print(f"Числа, делящиеся на 3: {divisible_by_3[:10]}...")
print(f"Числа, делящиеся на 5: {divisible_by_5[:10]}...")
'''

'''
numbers_str = input("Введите числа через пробел: ")
numbers = [int(x) for x in numbers_str.split()]
numbers = list(range(1, 101))

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]
divisible_by_3 = [num for num in numbers if num % 3 == 0]
divisible_by_5 = [num for num in numbers if num % 5 == 0]

print(f"Четные числа: {even_numbers[:10]}...")  # Показываем первые 10

sorted_numbers = sorted(numbers)
filtered_numbers = [num for num in sorted_numbers if num > 50]

print(f"Отсортированный список: {sorted_numbers}")
'''

'''
numbers_str = input("Введите числа через пробел: ")
numbers = [int(x) for x in numbers_str.split()]
print(f"Числа больше 50: {filtered_numbers}")
'''

'''

numbers = [int(x) for x in numbers_str.split()]
unique_numbers = []
seen = set()

for num in numbers:
    if num not in seen:
        unique_numbers.append(num)
        seen.add(num)
'''

'''
words_str = input("Введите слова через пробел: ")
words = words_str.split()

if words:
    longest = max(words, key=len)
    shortest = min(words, key=len)
    
    print(f"Самое длинное слово: {longest}")
    print(f"Самое короткое слово: {shortest}")
    
    alphabetically_sorted = sorted(words)
    print(f"Слова в алфавитном порядке: {alphabetically_sorted}")
    
    vowels = "аеёиоуыэюяaeiouAEIOU"
    vowel_words = [word for word in words if word[0] in 
    print(f"Слова, начинающиеся на гласную: {vowel_words}")
'''