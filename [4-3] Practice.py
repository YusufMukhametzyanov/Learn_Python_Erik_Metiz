# 4-3 . Считаем до 20: используйте цикл for для вывода чисел от 1 до 20 включительно .
# 4-4 . Миллион: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь циклом for
# для вывода чисел . (Если вывод занимает слишком много времени, остановите его нажатием
# Ctrl+C или закройте окно вывода .)
# 4-5 . Суммирование миллиона чисел: создайте список чисел от 1 до 1 000 000, затем вос-
# пользуйтесь функциями min() и max() и убедитесь в том, что список действительно начи-
# нается с 1 и заканчивается 1 000 000 . Вызовите функцию sum() и посмотрите, насколько
# быстро Python сможет просуммировать миллион чисел .
# 4-6 . Нечетные числа: воспользуйтесь третьим аргументом функции range() для создания
# списка нечетных чисел от 1 до 20 . Выведите все числа в цикле for .
# 4-7 . Тройки: создайте список чисел, кратных 3, в диапазоне от 3 до 30 . Выведите все числа
# своего списка в цикле for .
# 4-8 . Кубы: результат возведения числа в третью степень называется кубом . Например,
# куб 2 записывается в языке Python в виде 2**3 . Создайте список первых 10 кубов (то есть
# кубов всех целых чисел от 1 до 10) и выведите значения всех кубов в цикле for .
# 4-9 . Генератор кубов: используйте конструкцию генератора списка для создания списка
# первых 10 кубов.

# 4-3. Используем цикл for для вывода чисел в диапазоне он 1 до 20
# for _ in range(1, 21):
#     print(_)

# 4-4. Создаём лист из целочисленных значений от 1 до 1000000 и выводим их с помощью цикла for
# numbers_list = list(range(1, 1000001))
# for number in numbers_list:
#     print(number)
# 4-5
# my_list = list(range(1, 1000001))
# print(my_list)
# print(max(my_list))

# 4-6
# my_list = list(range(1, 21, 2))
# print(my_list)
# for number in my_list:
#     print(number)

# 4-7
# my_list = list(range(3, 31, 3))
# for number in my_list:
#     print(number)

# 4-8
# my_list = []
# for _ in range(1, 11):
#     cube = _ ** 3
#     my_list.append(cube)
# print(my_list)
# for number in my_list:
#     print(number)

# 4-9
print([value ** 3 for value in range(1, 11)]
)

