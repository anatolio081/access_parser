Для парсинга одного файла, требуется ввести следующую команду:
    python3 parser.py -f "access.log" --output "one_file_output.txt"
где:
    access.log-имя файла или абсолютный путь до файла для парсинга
    one_file_output.txt -имя файла для вывода.. Если параметр не вводить, он сохранится в output.txt

Для парсинга директории, требуется ввести следующую команду:
    python3 parser.py -d "acc_dir" --output "directory_output.txt"
где:
    acc_dir -имя директории или абсолютный путь до директориями с логами для парсинга
    directory_output.txt -имя файла для вывода.. Если параметр не вводить, он сохранится в output.txt