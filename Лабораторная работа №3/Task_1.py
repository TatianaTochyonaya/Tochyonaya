def index_search(items, needed_item):
    for index, item in enumerate(items):
        if item == needed_item:  # Если товар, который нужно найти, присутствует в списке, вернуть индекс
            return index
    return None  # Если товар не найден в списке, вернуть None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_search(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
