# # bicycles.py
# bicycles = ['trek ', 'cannondale', 'redline', 'specialized']
# print(bicycles.title())

# УПРАЖНЕНИЯ
# Попробуйте написать несколько коротких программ, чтобы получить предварительное
# представление о списках Python . Возможно, для упражнений из каждой главы стоит создать
# отдельную папку, чтобы избежать путаницы .
# 3-1 . Имена: сохраните имена нескольких своих друзей в списке с именем names . Выведите
# имя каждого друга, обратившись к каждому элементу списка (по одному за раз) .
# 3-2 . Сообщения: начните со списка, использованного в упражнении 3-1, но вместо вывода
# имени каждого человека выведите сообщение . Основной текст всех сообщений должен
# быть одинаковым, но каждое сообщение должно включать имя адресата .
# 3-3 . Собственный список: выберите свой любимый вид транспорта (например, мотоциклы
# или машины) и создайте список с примерами . Используйте свой список для вывода утверж-
# дений об элементах типа: «Я хотел бы купить мотоцикл Honda» .

# задаём список и печатаем каждый элемент с сообщением
# names = ['Muhammad','Luize', 'Amina', 'Aliya', 'Munira apa', 'Amir abiy'] # задали список и сохранили его в переменную names
# print("Пророк " + names[0] + " - печать пророков")
# print(names[1] + " моя любимая жена")
# print("Старшая дочка " + names[2] + " любит играть")
# print(names[3] + " начала активно исследовать этот мир")
# print("Благодарен Аллаху, что послал мне " + names[4])
# print(names[-1] + " инетересный собеседник")

# transport = ['Reno Logan', "BMV X5", 'Daewoo Nexia', 'Hyundai H1']
# print("\nI own " + transport[0])
# print('Father Luize own ' + transport[1])
# print('Earlier i have ' + transport[2])
# print('My dream is own ' + transport[-1])

my_list = ['Luize', 'Father', 'Munira apa', 'Amir abiy', 'Amina', 'Aliya'] # задаём новый список
# my_list.append('Anton')
# my_list[-1] = 'Muhammad'
# my_list.insert(0, 'Yusuf')
# my_list.insert(4, 'Mother')
#
# print(my_list) # выводим общий список гостей
# print(f"{my_list[-1]} won't come") # выводим кто прийти не сможет
# my_list[-1] = 'abduLlah'
# print(my_list)
# print("Poyavilis dopolnitelnie kvoti, 3 svobodnih mesta")
# my_list.insert(0, 'Guest1')
# my_list.insert(5, 'Guest2')
# my_list.append('Guest3')
# print(my_list)
# print('Na obeddenniy stol priglashautsya vsego 2 gostya')
#
# # удаляем последние элементы списка пока не останется 2 и выводим на печать сообщение с удалёнными
#
# while len(my_list) >= 3:
#     print(f'{my_list.pop()} mi sojaleem ob otmene priglasheniya')
# print(my_list)
# print(my_list[0] + ' priglashenie v sile')
# print(my_list[1] + ' priglashenie v sile')
# # удаляем последние 2 элемента спписка
# del my_list[0]
# print(my_list)
# del my_list[0]
# print(my_list)
a = len(my_list)
print('На обед приглашено ' + str(len(my_list)) + ' человек')





