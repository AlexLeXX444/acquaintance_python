# На столе стоит две корзины с яблоками. Корзина a и корзина b. Введите количество яблок с клавиатуры. Затем поменяйте содержимое корзин местами и выведите результат.
busket1 = int(input('Введите количество яблок в первой корзине:'))
busket2 = int(input('Введите количество яблок во второй корзине:'))

if busket1 != busket2:
    busket1 = busket1 + busket2
    busket2 = busket1 - busket2
    busket1 = busket1 - busket2
    print(f'Яблок в первой корзине {busket1}. Яблок во второй корзине {busket2}.')
else:
    print('Количество яблок в корзинах равное.')