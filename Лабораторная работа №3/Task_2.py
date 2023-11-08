# TODO Напишите функцию find_common_participants
def find_common_participants(string1, string2, separator=','):
    group1 = string1.split(separator)  # Разделение строк по запятым
    group2 = string2.split(separator)
    common_participants = list(set(group1).intersection(group2))  # Список общих участников среди двух групп
    common_participants.sort()  # Сортировка списка в алфавитном порядке
    return common_participants  # Возврат списка

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))
