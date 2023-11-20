import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as file:  # Открытие файла input.csv для чтения
        csv_data = [column for column in csv.DictReader(file)]  # Возвращение каждого столбца в виде словаря
    with open(OUTPUT_FILENAME, 'w') as f:  # Открытие файла output.json для записи
        json.dump(csv_data, f, indent=4)  # Сериализация данных в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
