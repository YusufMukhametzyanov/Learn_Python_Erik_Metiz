# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# for alien in aliens:
#     print(alien)

# создание пустого списка
aliens = []
# создание 30 зелёных пришельцев
for alien_number in range(30):
    new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# вывод 5 первых пришельцев
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'
    if alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['point'] = 15
        alien['speed'] = 'fast'
for alien in aliens[:5]:
    print(alien)
print('\t...')
# вывод всего количества созданных пришельцев
# print(f'Total number of aliens: {len(aliens)}')


