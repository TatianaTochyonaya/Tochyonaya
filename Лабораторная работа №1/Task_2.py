pages = 100
lines_per_page = 50
symbols_per_line = 25
BYTES_PER_SYMBOL = 4

volume_of_disk = 1.44 * 1024 * 1024  # Объем дискеты в байтах
count_of_symbols = symbols_per_line * lines_per_page * pages  # Общее количество символов в книге
volume_of_symbols = count_of_symbols * BYTES_PER_SYMBOL  # Объем памяти для хранения кода всех символов

count_of_books = int(volume_of_disk // volume_of_symbols)  # Количество книг, которые можно поместить на дискету

print("Количество книг, помещающихся на дискету:", count_of_books)
