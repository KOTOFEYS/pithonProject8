def custom_wrihte(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}

    for string in strings:
        strings_positions[(len(strings_positions) + 1,file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_wrihte('test.txt', info)
for elem in result.items():
    print(elem)