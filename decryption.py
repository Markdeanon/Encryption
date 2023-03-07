import pyAesCrypt
import os
# функция дешифрования файла
def decryption(file, password):

    # задаем размер буфера
    buffer_size = 512 * 1024

    # вызываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )

    # чтобы видеть результат, выводим на печать имя зашифрованного файщла
    print("[Файл '" + str(os.path.split(file)[0]) + "' расшифрован]")

    # удаляем исходный файл
    os.remove(file)

# функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в указанной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если нашелся файл, то дешифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находится директория, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)

password = input("Введите пароль для расшифровки: ")
# в скобках внизу указываем расположение директории
walking_by_dirs("", password)