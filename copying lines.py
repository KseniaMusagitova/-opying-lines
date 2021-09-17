# Копирование строк (1,2,4,5,6), расположенных в исходном файле, в новый текстовый файл

with open('source_text.txt', 'r') as file1:
    with open('new_text.txt', 'a') as file2:
        lines = [1, 2, 4, 5, 6]
        for n, line in enumerate(file1):
            if (n + 1) in lines:
                file2.write(line)

# Копирование строк (в диапазоне от 1 до 3), расположенных в исходном файле, в новый текстовый файл

with open('source_text.txt', 'r') as f1:
    with open('new_text.txt', 'a') as f2:
        lines = range(1, 3)
        for n, line in enumerate(f1):
            if (n + 1) in lines:
                f2.write(line)




