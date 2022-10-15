BYTES_ONE_CHAR = 1  # размер одного символа в байтах

# никаких магических чисел
pages = 100
lines = 50
chars = 25

total_chars = chars * lines # символов на странице книги
total_bytes = total_chars * pages # размер книги в байтах

disk_size = 1.44 * (2**20) # размер дискеты в байтах

print(disk_size // total_bytes)  # количество книг на дискете
