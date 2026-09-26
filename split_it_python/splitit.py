# SplitIt v1.0 — Калькулятор совместных расходов
# Автор: vllln

import datetime
import os
def clear():
     os.system('cls' if os.name == 'nt' else 'clear')

current_month = datetime.datetime.now().strftime('%B_%Y')
file_name = f'{current_month}_history.txt'


total_sum = 0
with open(file_name, 'a', encoding='utf-8') as file:
            file.write('\n' + '='*20 + '\nНОВЫЙ ВЕЧЕР\n' + '='*20 + '\n')
            
privet = '----Честный чек----'

while True:
    clear()
    print(privet)

    bill = input('\nВведите сумму чека или "стоп" для выхода: ')
    if bill.lower() == 'стоп':
        break
    
    try:  
        bill = float(bill)
        people = int(input('Введите кол-во гостей: '))
        tips_percent = int(input('Сколько процентов чаевых оставим? (10, 15, 20)'))
        bill_tips = bill*(1 + tips_percent/100)
            
        # Рассчитываем сумму каждого + процент
        result = round(bill_tips / people, 2)
        total_sum += bill_tips
        total_sum = round(total_sum, 2)

        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(f'Чек: {bill} руб. Гостей: {people}, С каждого: {result}\n')
            file.write("----------\n")

        if result >= 1000:
            print('Ого, как дорого!')
        else:
            print(f'\nВсего {result}? Дальше гуляем!')
            print(f'Каждый должен скинуться по {result} руб.')
        print(f"Итого за вечер: {total_sum}")    
        input("\nНажмите Enter, чтобы продолжить...")
    # Если ввод не цифр:
    except ValueError:
        print('Что-то пошло не так! Может попробуете ввести цифры?')
    



