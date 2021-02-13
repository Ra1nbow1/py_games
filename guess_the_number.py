# Угадай число
# Рандомное число, которые нужно угадать за 7 попыток
import random

number = random.randint(1, 20) # Рандом 1-20

print('!', number) # Загаданное число

for i in range(7):
    user = int(input())
    
    if user > number:
        print('Загаданое число меньше. Попыток - ', 6-i)
    if user < number:\
        print('Загаданое число больше. Попыток - ', 6-i)
    if user == number:
        print('Угадал - ', number)
        break
    if i == 7:
        print('Ты проиграл, попытки закончились')
