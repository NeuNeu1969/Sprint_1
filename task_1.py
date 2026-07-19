## Задание 1
values = '1h 45m,360s,25m,30m 120s,2h 60s'

sum_minutes = 0

# выделяем значения по запятой
items = values.split(',')

for item in items:
    # выделяем цифры часов и минут
    parts = item.split(' ')
    
    for part in parts:
        # проверка на часы
        if 'h' in part:
            hours = int(part.replace('h', ''))
            sum_minutes += hours * 60
        # проверка на минуты
        elif 'm' in part:
            minutes = int(part.replace('m', ''))
            sum_minutes += minutes
        # проверка на секунды
        elif 's' in part:
            seconds = int(part.replace('s', ''))
            sum_minutes += seconds / 60

print(sum_minutes)