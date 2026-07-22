# Подключаем "красивую печать" - подсказал ИИ.
from pprint import pprint

types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

# Формирование списка без дубликатов
def remove_duplicates(tickets):
    # Список уже встреченных тикетов
    meet = []
    # Результат метода
    result = {}
    # Цикл перебора справочника по уровню
    for lvl in tickets:
        # Обнуляем список для нового уровня
        unique_list = []
        # Цикл перебора элемента
        for ticket in tickets[lvl]:
            # Проверка встречали или нет
            if ticket not in meet:
                # Добавляем в список без дубликатов
                unique_list.append(ticket)
                # Добавляем проверенный в список встреченных
                meet.append(ticket)
        # Добавляем уникальный список в результат
        result[lvl] = unique_list
    return result

# Привязка уровня критичности к тикетам
def link_types_and_tickets(types, tickets):
    # Получаем результат метода удаления дубликатов
    unique_tickets = remove_duplicates(tickets)
    # Результат метода
    result = {}
    # Цикл по уровню критичности
    for lvl in types:
        # Привязка критичности к тикету
        result[types[lvl]] = unique_tickets[lvl]
    return result

# Синтаксис использования "красивой печати" подсказал ИИ
pprint(link_types_and_tickets(types, tickets))