numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers_before_none = numbers[0:4]  # Числа до пропущенного элемента
numbers_after_none = numbers[5:]  # Числа после пропущенного элемента
count_of_elements = len(numbers)  # Общее количество элементов в списке

# Расчёт среднего арифметического
average_of_numbers = (sum(numbers_before_none) + sum(numbers_after_none)) / count_of_elements
numbers[4] = average_of_numbers  # Замена пропущенного элемента средним арифметическим

print('Измененный список:', numbers)
