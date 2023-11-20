# TODO решите задачу
import json


def task() -> float:
    with open('input.json') as f:  # Чтение данных из файла input.json, десериализация в объект Python
        json_data = json.load(f)

    # Сумма произведений "score" * "weight" в каждом словаре
    sum_of_multiplication = sum([item['score'] * item['weight'] for item in json_data])
    return round(sum_of_multiplication, 3)  # Округление суммы произведений до 3 знаков после запятой

print(task())
