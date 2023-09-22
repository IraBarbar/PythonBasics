from year import test_date
from sys import argv

lst = ['21.01.2023', '29.02.1903', '29.02.2000', '31.04.2010', '01.01.10000', 'o1.01.2010']

for k in lst:
    print(f'{k:<12}: {test_date(k)}')

date = '.'.join(argv[1:4])
test_date(date)  # но как я не пыталась модуль запусить не могу через командную строку, а напрямую через функцию могу
