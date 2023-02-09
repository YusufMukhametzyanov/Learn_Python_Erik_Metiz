# 4-10. Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
# который делает следующее .
# Выводит сообщение «The first three items in the list are:», а затем использует срез для
# вывода первых трех элементов из списка .
# Выводит сообщение «Three items from the middle of the list are:», а затем использует
# срез для вывода первых трех элементов из середины списка .
# Выводит сообщение «The last three items in the list are:», а затем использует срез для
# вывода последних трех элементов из списка .

# number_list = list(range(1, 11))
# print(number_list)
# print(f'The first three items in the list are: {number_list[:3]}')
# print(f'Three items from the middle of the list are: {number_list[len(number_list)//3:-(len(number_list)//3)]}')
# print(f'The last three items in the list are: {number_list[-3:]}')

# 4-11 . Моя пицца, твоя пицца: начните с программы из упражнения 4-1 . Создайте копию
# списка с видами пиццы, присвойте ему имя friend_pizzas . Затем сделайте следующее .
# Добавьте новую пиццу в исходный список .
# Добавьте другую пиццу в список friend_pizzas .
# Докажите, что в программе существуют два разных списка . Выведите сообщение «My
# favorite pizzas are:», а затем первый список в цикле for . Выведите сообщение «My
# friend’s favorite pizzas are:», а затем второй список в цикле for . Убедитесь в том, что
# каждая новая пицца находится в соответствующем списке .

# pizza_list = ['Вегетарианская: Гавайская', 'Дьябола: Кальцоне', 'Каприччоза: Маргарита']
# friend_pizzas = pizza_list[:]
# pizza_list.append('Маринара: Неаполитанская')
# friend_pizzas.append('Охотничья: Пицца с морепродуктами')
# print('My favorite pizzas are: ')
# for pizza in pizza_list:
#     print(pizza)
# print("\nMy friend's favorite pizzas are: ")
# for pizza in friend_pizzas:
#     print(pizza)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

for food in my_foods:
    print(food)
print('\n')
for food in friend_foods:
    print(food)





