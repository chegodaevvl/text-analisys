letters_count = dict()


def line_processing(source_line: str):
    """
        Функция обработки строки для подсчета количества уникальных букв в ней
    :param source_line: str - Строка для обработки
    """
    for char in source_line:
        if char.isalpha():
            if char in letters_count:
                letters_count[char] += 1
            else:
                letters_count[char] = 1


with open('text.txt', 'r', encoding='utf8') as source_file:
    for file_line in source_file:
        line_processing(file_line.lower())
total_letters = sum(letters_count.values())
for key in sorted(letters_count.keys()):
    letter_frequency = round(letters_count[key] / total_letters, 4) * 100
    print('{} - {}%'.format(key, letter_frequency))
print('Работа программы завершена!')
