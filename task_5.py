# Подключаем "красивую печать" - подсказал ИИ.
from pprint import pprint

# Сборка класса 
class TestCase:

    # Инициализация полей 
    def __init__(self, steps={}, result=None):
        self.steps = steps
        self.result = result

    # Метод добавляет шаг
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    # Метод удаляет шаг
    def delete_step(self, step_number):
        del self.steps[step_number]

    # Метод устанавливает ожидаемый результат
    def set_result(self, result):
        self.result = result

    # Метод печатает тест-кейс в заданном формате.
    def get_test_case(self):
        # Синтаксис использования "красивой печати" подсказал ИИ
        pprint({'Шаги': self.steps, 'Ожидаемый результат': self.result}) 


test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()