def get_month_name(month_number):
    months = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень',
               'Червень', 'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return 'Невірний номер місяця'

month_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_names = list(map(get_month_name, month_numbers))
print(month_names)