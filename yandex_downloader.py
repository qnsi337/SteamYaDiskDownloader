#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import re
import requests
import json
from urllib.parse import urlencode, urlparse, parse_qs
import time


# Цвета для вывода в консоль
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'


def colored_print(text, color=None, bold=False):
    """
    Печатает текст с цветом.
    """
    color_code = getattr(Colors, color.upper(), '') if color else ''
    bold_code = Colors.BOLD if bold else ''

    # Windows требует инициализации для поддержки цветов
    if sys.platform == 'win32':
        os.system('')  # Включаем ANSI на Windows

    print(f"{bold_code}{color_code}{text}{Colors.END}")


def simple_extract_yandex_links(text_content):
    """
    Извлекает простые ссылки Яндекс из текстового содержимого.

    Args:
        text_content (str): Текстовое содержимое, из которого нужно извлечь ссылки

    Returns:
        list: Список найденных ссылок
    """
    # Разбиваем текст на строки и фильтруем ссылки Яндекс Диск
    links = [line.strip() for line in text_content.split('\n')
             if line.strip() and ('yadi.sk' in line or 'disk.yandex' in line)]
    return links


def download_yandex_file(url, folder, max_retries=3):
    """
    Скачивает файл по публичной ссылке Яндекс.Диск с повторными попытками.

    Args:
        url (str): Публичная ссылка на файл
        folder (str): Папка для сохранения
        max_retries (int): Максимальное количество повторных попыток

    Returns:
        bool: True если успешно, False в случае ошибки
    """
    for attempt in range(max_retries):
        try:
            # Базовый URL API Яндекс.Диск
            base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'

            # Получаем загрузочную ссылку
            colored_print(f"Получение прямой ссылки для: {url} (Попытка {attempt + 1}/{max_retries})", "cyan")
            final_url = base_url + urlencode(dict(public_key=url))
            response = requests.get(final_url)

            # Проверяем успешность запроса
            if response.status_code != 200:
                colored_print(f"✗ Ошибка при получении прямой ссылки: {response.text}", "red")

                # Ждем перед следующей попыткой
                if attempt < max_retries - 1:
                    time.sleep(2)  # Пауза между попытками
                continue

            # Извлекаем прямую ссылку из ответа
            try:
                download_url = response.json()['href']
            except (json.JSONDecodeError, KeyError):
                colored_print(f"✗ Не удалось получить прямую ссылку из ответа API", "red")

                # Ждем перед следующей попыткой
                if attempt < max_retries - 1:
                    time.sleep(2)  # Пауза между попытками
                continue

            # Получаем имя файла из URL или генерируем имя
            try:
                # Пытаемся получить имя файла из параметра filename
                filename = parse_qs(urlparse(download_url).query).get('filename', [''])[0]
                if not filename:
                    # Альтернативный вариант - пытаемся получить из Content-Disposition
                    head_response = requests.head(download_url)
                    content_disp = head_response.headers.get('Content-Disposition', '')
                    filename_match = re.search(r'filename="?([^";]+)"?', content_disp)
                    if filename_match:
                        filename = filename_match.group(1)
            except:
                filename = ''

            # Если имя не получено, генерируем его
            if not filename:
                public_key = url.split('/')[-1].split('?')[0]
                filename = f"yadisk_file_{public_key}"

            # Полный путь для сохранения файла
            file_path = os.path.join(folder, filename)

            # Загружаем файл и сохраняем его
            colored_print(f"Скачивание файла: {filename}", "blue")
            download_response = requests.get(download_url)

            with open(file_path, 'wb') as f:
                f.write(download_response.content)

            colored_print(f"✓ Файл сохранен: {file_path}", "green")
            return True

        except Exception as e:
            colored_print(f"✗ Произошла ошибка при попытке {attempt + 1}: {str(e)}", "red")

            # Ждем перед следующей попыткой
            if attempt < max_retries - 1:
                time.sleep(2)  # Пауза между попытками

    colored_print(f"✗ Не удалось скачать файл после {max_retries} попыток", "red")
    return False


def download_from_file(links_file, output_folder):
    """
    Скачивает файлы по ссылкам из текстового файла.

    Args:
        links_file (str): Путь к файлу со ссылками
        output_folder (str): Папка для сохранения файлов
    """
    # Создаем папку, если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        colored_print(f"Создана папка: {output_folder}", "blue")

    # Читаем ссылки, пропуская пустые строки
    try:
        with open(links_file, 'r', encoding='utf-8', errors='ignore') as file:
            links = [line.strip() for line in file
                     if line.strip() and ('yadi.sk' in line or 'disk.yandex' in line)]
    except Exception as e:
        colored_print(f"Ошибка при чтении файла {links_file}: {str(e)}", "red")
        return

    total_links = len(links)
    if total_links == 0:
        colored_print("Ссылки Яндекс.Диск не найдены. Проверьте файл или текст.", "yellow")
        return

    colored_print(f"Найдено {total_links} ссылок Яндекс.Диск:", "cyan", bold=True)
    for i, link in enumerate(links, 1):
        colored_print(f"  {i}. {link}", "cyan")

    colored_print("\nНачинаю скачивание файлов...", "blue", bold=True)

    success_count = 0
    # Скачиваем каждый файл
    for i, link in enumerate(links, 1):
        colored_print(f"\n[{i}/{total_links}] Обработка ссылки: {link}", "blue")
        if download_yandex_file(link, output_folder):
            success_count += 1

    colored_print(f"\nЗагрузка завершена. Успешно скачано {success_count} из {total_links} файлов.", "green", bold=True)
    colored_print(f"Файлы сохранены в папке: {output_folder}", "green")

    # Спрашиваем пользователя, нужно ли обрабатывать файлы
    colored_print("\nОбработать скачанные файлы? (переименование и запись данных в data.txt)", "yellow")
    colored_print("Нажмите Enter для подтверждения или введите 'no' для отмены:", "yellow")
    process_choice = input()

    if process_choice.lower() not in ['no', 'n', 'нет', 'н']:
        # После скачивания обработаем файлы
        process_downloaded_files(output_folder)
    else:
        colored_print("Обработка файлов отменена.", "yellow")


def process_downloaded_files(folder):
    """
    Обрабатывает скачанные файлы с данными в формате логин+пароль+почта+пароль_от_почты.mafile.
    Переименовывает их в логин.mafile и записывает данные в data.txt.

    Args:
        folder (str): Папка с файлами
    """
    colored_print("\nОбработка скачанных файлов...", "blue", bold=True)

    # Создаем файл для записи данных
    data_file_path = os.path.join(folder, "data.txt")
    processed_count = 0

    with open(data_file_path, 'w', encoding='utf-8') as data_file:
        # Перебираем все файлы в папке
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)

            # Пропускаем data.txt и директории
            if filename == "data.txt" or not os.path.isfile(file_path):
                continue

            # Проверяем, соответствует ли файл формату и имеет расширение .mafile
            if filename.endswith('.mafile') and '+' in filename:
                try:
                    # Разбираем имя файла на части
                    parts = filename.rsplit('.', 1)[0].split('+')

                    # Если файл имеет правильный формат с 4 частями
                    if len(parts) >= 4:
                        login = parts[0]
                        password = parts[1]
                        email = parts[2]
                        email_password = parts[3]

                        # Формируем новое имя файла
                        new_filename = f"{login}.mafile"
                        new_file_path = os.path.join(folder, new_filename)

                        # Переименовываем файл
                        if file_path != new_file_path:  # Избегаем переименования, если имя уже в нужном формате
                            # Если файл уже существует, удаляем его
                            if os.path.exists(new_file_path):
                                os.remove(new_file_path)
                                colored_print(f"Заменен существующий файл: {new_filename}", "yellow")

                            os.rename(file_path, new_file_path)
                            colored_print(f"Переименован: {filename} -> {new_filename}", "green")

                        # Записываем данные в файл
                        data_line = f"{login}:{password}:{email}:{email_password}\n"
                        data_file.write(data_line)
                        processed_count += 1

                except Exception as e:
                    colored_print(f"Ошибка при обработке файла {filename}: {str(e)}", "red")

    if processed_count > 0:
        colored_print(f"\nОбработка файлов завершена. Обработано файлов: {processed_count}", "green", bold=True)
        colored_print(f"Данные сохранены в файле: {data_file_path}", "green")
    else:
        colored_print("\nНе найдено файлов для обработки в указанном формате.", "yellow")


if __name__ == "__main__":
    # Если скрипт запущен с аргументами
    if len(sys.argv) > 1:
        # Если передана только ссылка, используем папку accs
        if len(sys.argv) == 2:
            sys.argv.append('accs')

        # Скачиваем файл по ссылке
        folder = sys.argv[2]
        url = sys.argv[1]

        if not os.path.exists(folder):
            os.makedirs(folder)

        download_yandex_file(url, folder)

        # Спрашиваем, нужно ли обрабатывать файлы
        colored_print("\nОбработать скачанные файлы? (переименование и запись данных в data.txt)", "yellow")
        colored_print("Нажмите Enter для подтверждения или введите 'no' для отмены:", "yellow")
        process_choice = input()

        if process_choice.lower() not in ['no', 'n', 'нет', 'н']:
            # Обрабатываем скачанные файлы
            process_downloaded_files(folder)
        else:
            colored_print("Обработка файлов отменена.", "yellow")
    else:
        # Интерактивный режим
        colored_print("Вы можете ввести путь к файлу со ссылками или просто нажать Enter для использования 'links.txt'",
                      "cyan")
        custom_path = input("Путь к файлу (или Enter для 'links.txt'): ")

        # Используем введенный путь или значение по умолчанию
        links_file = custom_path.strip() if custom_path.strip() else "links.txt"

        # Запрашиваем путь к папке для сохранения
        colored_print("Вы можете ввести путь к папке для сохранения или просто нажать Enter для использования 'accs'",
                      "cyan")
        custom_folder = input("Папка для сохранения (или Enter для 'accs'): ")

        # Используем введенный путь или значение по умолчанию
        output_folder = custom_folder.strip() if custom_folder.strip() else "accs"

        # Запускаем загрузку
        download_from_file(links_file, output_folder)

    # Ожидаем нажатия Enter для выхода
    colored_print("\n✓ Все операции успешно завершены!", "green", bold=True)
    colored_print("Нажмите Enter для выхода...", "blue")
    input()