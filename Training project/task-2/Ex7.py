try:
    a = int(input('Введите среднесуточный объем записываемых данных: '))
    b = ((3000 * 500)/a)/365
    b1 = b/4
    b2 = b/10
    print('\nМинимальный срок службы - ',round(b2,2), '\nПриблизительный срок службы - ',round(b1,2))
    input()
except:
    print('Вы ввели неверные значения!')
    input()