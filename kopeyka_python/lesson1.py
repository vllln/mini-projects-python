def show_total(item_list):
    total = 0
    for stuff in basket:
        total += stuff['цена']
    print('-' * 20)
    print(f'Итого к оплате: {total} руб.')
    print('=' * 20)

try:
    with open('balance.txt', 'r', encoding='utf-8') as f:
        balance = float(f.read().strip())
    print(f'Твой текущий баланс: {balance} руб.')
except FileNotFoundError:
    balance = float(input('Файла с балансом нет. Введи начальный баланс: '))



basket = []

while True:
    name = input('Что купили? Или "стоп" для выхода: ')

    if name.lower() == 'стоп':
        break

    price = int(input(f'Сколько стоит {name}? '))
    balance -= price
    item = {'название': name, 'цена': price}
    basket.append(item)

print('\nВ твоей корзине сейчас: ')
for stuff in basket:
    print(f"Товар: {stuff['название']} | Цена: {stuff['цена']} руб.")

show_total(basket)


with open('check.txt', 'a', encoding='utf-8') as file:
    file.write('\n---НОВЫЕ ПОКУПКИ---\n')
    for stuff in basket:
        file.write(f'{stuff['название']}: {stuff['цена']} руб \n')

    total = sum(item['цена'] for item in basket)
    file.write(f'ИТОГО ПОТРАЧЕНО: {total} руб. | ОСТАТОК: {balance}\n')

with open('balance.txt', 'w', encoding='utf-8') as f:
    f.write(str(balance))
print(f'Новый баланс сохранен: {balance}')

print('Чек сохранен в файл check.txt')
