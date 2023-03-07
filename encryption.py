import pyAesCrypt
import os
# функция шифрования
def encryption(file, password):

    # задаем размер буфера
    buffer_size = 512 * 1024

    # вызываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # чтобы видеть результат, выводим на печать имя зашифрованного файщла
    print("[Файл '" + str(os.path.split(file)[0]) + "' зашифрован]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если нашелся файл, то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находится директория, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для шифрования: ")
# в скобках внизу указываем расположение директории
walking_by_dirs("", password)