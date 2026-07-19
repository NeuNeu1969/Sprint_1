new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

# Перенос задачи 'task_005'
completed_tasks.append(new_tasks.pop(-1))

# Удаление задачи 'task_007'
new_tasks.remove('task_007')

# Вывод на экран задачи с изменённым приоритетом
print(new_tasks[-1])
