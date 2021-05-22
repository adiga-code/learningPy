from random import choice
print('Здравствуйте, выберите лотерейный билет')
symbols = [1, 2, 4, 3, 6, 7, 5, 9, 8, 0, 'a', 't', 'g', 'h', 'q']
rand_symb1 = choice(symbols)
rand_symb2 = choice(symbols)
rand_symb3 = choice(symbols)
rand_symb4 = choice(symbols)
rand_ch = f'{rand_symb1}_{rand_symb2}_{rand_symb3}_{rand_symb4}'
print(f'\nБилет {rand_ch} выигрышный')

my_ticket = [1, 2, 4, 3, 6, 7, 5, 9, 8, 0, 'a', 't', 'g', 'h', 'q']
def rand_choise():
    rand_symb11 = choice(symbols)
    rand_symb22 = choice(symbols)
    rand_symb33 = choice(symbols)
    rand_symb44 = choice(symbols)
    rand_ch1 = f'{rand_symb11}_{rand_symb22}_{rand_symb33}_{rand_symb44}'
    return rand_ch1
print(rand_choise)
if rand_ch1==rand_ch:
    print('Поздравляем, вы выиграли')
else:
    print(rand_choise)
    





























