# 5-8

# names_list = ['Yuriy', 'Luiza', 'Amina', 'Aliya', 'Yasin', 'admin']
#
# for name in names_list:
#     if name == 'admin':
#         print(f'Hello {name}, would you like to see a status report?')
#     else:
#         print(f'Hello {name}, thank you for logging in again.')

# 5-9

# names_list = ['Yuriy', 'Luiza', 'Amina', 'Aliya', 'Yasin', 'admin']
#
# names_list.clear()
#
# if names_list:
#     for name in names_list:
#         if name == 'admin':
#             print(f'Hello {name}, would you like to see a status report?')
#         else:
#             print(f'Hello {name.title()}, thank you for logging in again.')
# else:
#     print('We need to ind some users.')

# 5-10

# current_list = ['Yuriy', 'Luiza', 'Amina', 'Aliya', 'Yasin', 'admin']
# new_list = ['YURIY', 'Ramil', 'Lilya', 'Luiza', 'Munira']
#
# if current_list or new_list:
#     for i in new_list:
#         if i in current_list or i.title() in current_list or i.lower() in
#         current_list or i.upper() in current_list:
#             print(f'Name {i} unavailable')
#         else:
#             print(f'Name {i} available')
#
# else:
#     print('Enter names')

# 5-11

numbers_list = []

for number in range(1, 10):
    numbers_list.append(number)

if numbers_list:
    for number in numbers_list:
        if number == 1:
            print(f'{number}st')
        elif number == 2:
            print(f'{number}nd')
        elif number == 3:
            print(f'{number}rd')
        else:
            print(f'{number}th')










