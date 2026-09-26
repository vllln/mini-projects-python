import random

# Выводим суть игры в самом начале
print('Суть игры: компьютер загадывает число от 1 до 3, а вам нужно его угадать за 3 попытки!')

number_guesses = 0
num = random.randint(1,3)

for i in range(3):
    # Просим пользователя ввести число перед каждым вводом
    print('Введите ваше число от 1 до 3:')
    nm = int(input())
    
    if nm == num:
        number_guesses = number_guesses + 1
        print('Вау, вы настоящий волшебник!')
    else:
        print('Увы, в этот раз не повезло!')

print('Количество отгадок:', number_guesses)        
        
if number_guesses >=2:
    print('Вау, вы сегодня были в ударе!')
else:
    print('Неплохой результат, но можно лучше!')
