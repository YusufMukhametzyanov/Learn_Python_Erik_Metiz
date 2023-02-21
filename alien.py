# alien_0 = {'color': 'green', 'points': 5}  # создали словарь с 2 ключами
# new_points = alien_0['points']  # записали в переменную new_points значение ключа
#                                 # 'points'
#
# # print(f'You just earned {new_points} points!')
#
# alien_0['x_position'] = 0   # добавили в словарь новую позицию
# alien_0['y_position'] = 25  # ~
#
# print(alien_0) # печатаем полный словарь alien_0
#
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
#
# alien_0['color'] = 'blue'
# print(alien_0)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f'Original position = {alien_0["x_position"]}')

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'New position = {alien_0["x_position"]}')


