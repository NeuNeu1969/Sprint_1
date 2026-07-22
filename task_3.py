world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'
# Печатаем содержимое словаря + новый элемент, получаем пару сразу
for year, country_name in world_champions.items():
    print(year, '-', country_name)

# исправлено условие проверки
country = 'Италия'
if country in world_champions:
    print('Италия cтановилась чемпионом мира по футболу в 21 веке!')
else:
    print('Италия не выигрывала чемпионат мира по футболу в 21 веке.')