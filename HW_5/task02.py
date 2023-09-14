# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

lst_names = ['Ivan', 'Ira', 'Platon']
lst_bid = [100, 200, 300]
lst_bonus_pr = ['10.10%', '10.10%', '10.10%']


gen_dict_bonus = {key: val for key, val in
                  zip(lst_names,
                      [num2 * num1 / 100 for num1, num2 in
                       zip(lst_bid,
                           list(map(lambda x: float(x[:-1]), lst_bonus_pr)))])}

for k, v in gen_dict_bonus.items():
    print(f'{k:{len(max(gen_dict_bonus))}} : {v}')
