favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# for name, language in favorite_languages.items():   # перебираем ключи и
# значения
#     print(f'{name.title()}`s favorite language is {language.title()}.')
# print('\n')
# for name in favorite_languages.keys():
#     print(name.title())
# friends = ['jen', 'edward']
# for name in sorted(favorite_languages.keys()):
#     print(name.title())
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f'\t{name.title()}, I see you love {language}')

# for language in set(favorite_languages.values()):
#     print(language.upper())
language_list = []

for name in favorite_languages.keys():
    language_list.append(name)

print(language_list)

language_list.append('Sonya'), language_list.append('Nikolay')
language_list.append("Andrew")

print(language_list)

for name in language_list:
    if name in favorite_languages:
        print(f'{name.title()} благодарим за пройденный опрос')
    else:
        print(f'{name.title()} предлагаем Вам пройти опрос')


