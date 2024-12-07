# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим общих участников и сортируем их в алфавитном порядке
    common_participants = sorted(participants1.intersection(participants2))

    return common_participants

# Пример использования
group1 = "Иванов,Петров,Сидоров"
group2 = "Петров,Сидоров,Смирнов"
common = find_common_participants(group1, group2)
print(common)

# TODO Провеьте работу функции с разделителем отличным от запятой
