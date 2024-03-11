import difflib
import sys
import re

def read_file(filename):
    """Читает файл и возвращает содержимое без всех пробелов."""
    with open(filename, 'r') as file:
        # Удаляем все пробелы из каждой строки
        return [re.sub(r'\s+', '', line).lower() for line in file]

def compare_files(file_path1, file_path2):
    """Сравнивает содержимое двух файлов и выводит отличающиеся строки, игнорируя пробелы."""
    content1 = read_file(file_path1)
    content2 = read_file(file_path2)

    # Получаем различия между файлами
    d = difflib.Differ()
    diff = list(d.compare(content1, content2))

    # Проверяем, есть ли отличия после удаления пробелов
    has_differences = any(line.startswith(('-', '+')) for line in diff)

    if has_differences:
        print("Отличия между файлами (игнорируя пробелы):")
        for line in diff:
            if line.startswith('+ '):
                print(f"В {file_path2}: {line[2:]}")
            elif line.startswith('- '):
                print(f"В {file_path1}: {line[2:]}")
    else:
        print("Файлы идентичны после удаления всех пробелов.")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Использование: script.py file1.txt file2.txt")
    else:
        file_path1 = sys.argv[1]
        file_path2 = sys.argv[2]
        compare_files(file_path1, file_path2)
