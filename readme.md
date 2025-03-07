# Steam YaDisk Downloader | Скачивание Steam аккаунтов с Яндекс.Диска

[English](#english) | [Русский](#russian)

<a name="english"></a>
## English

### Steam Account Downloader from Yandex.Disk

A simple utility that helps you download Steam accounts from Yandex.Disk links, automatically rename the files, and extract login information.

### Quick Start

1. **Download the program** from the [Releases](https://github.com/qnsi337/SteamYaDiskDownloader/releases) section
2. **Extract the archive** to any folder
3. **Create a `links.txt` file** and add your Yandex.Disk links (one per line)
4. **Run `SteamYaDiskDownloader.exe`**
5. **Follow the on-screen instructions**

### What This Tool Does

This program allows you to:
1. Automatically download multiple Steam accounts from Yandex.Disk links
2. Rename files to a convenient format (`login.mafile`)
3. Create a text file with account data (`data.txt`) in an easy-to-use format

### Detailed Instructions

#### Step 1: Preparation
1. Download `SteamYaDiskDownloader.exe` from the [Releases](https://github.com/qnsi337/SteamYaDiskDownloader/releases) section
2. Extract the archive to any folder

#### Step 2: Creating a List of Links
1. Create a text file `links.txt` in the same folder as the program
2. Add your Yandex.Disk links to the file (one link per line)

#### Step 3: Downloading Files
1. Run the `SteamYaDiskDownloader.exe` program
2. When prompted for the file path, simply press Enter (the program will automatically use the `links.txt` file)
3. When prompted for the save folder, simply press Enter to use the default `accs` folder
4. Wait for the files to finish downloading

#### Step 4: Processing Files
1. After downloading, press Enter to convert the files and create `data.txt`
2. The program will rename files from the format `login+password+email+email_password.mafile` to `login.mafile`
3. It will also create a `data.txt` file with all account credentials

### What's in the data.txt File?

After conversion, the `data.txt` file will contain lines in the format:
```
login:password:email:email_password
```

For example:
```
steamuser123:pass123:user123@mail.ru:mailpass123
```

This is convenient for quickly copying data when logging in through SDA.

### Example links.txt Content

```
https://yadi.sk/d/435AGH5Ppd9pGw
https://disk.yandex.by/d/435AGH5Ppd9pGw
```

### Important Information

- All files are saved to the `accs` folder (created automatically)
- The program works with Yandex.Disk links (yadi.sk or disk.yandex.ru)
- If a file named `login.mafile` already exists, it will be replaced with the new file
- **It is recommended to change the account credentials after receiving them!**

### System Requirements

- Windows 7/8/10/11
- Internet connection for downloading files
- No installation of Python or other programs required

### FAQ

**Q: Is this program safe?**
A: Yes, the program simply downloads files from Yandex.Disk links and does not send any data to other servers.

**Q: Do I need to install the program?**
A: No, just download the EXE file and run it.

**Q: How do I use the mafile file?**
A: The .mafile file needs to be imported into Steam Desktop Authenticator (SDA) or another program for working with Steam accounts, such as TradeOn SDA.

**Q: Can I download just one account?**
A: Yes, just add a single link to the links.txt file.

**Q: What should I do if the program doesn't start?**
A: Make sure you've fully extracted the archive and have permission to run the program. If you encounter problems, contact the seller.

---

<a name="russian"></a>
## Русский

### Загрузчик Steam аккаунтов с Яндекс.Диска

Простая утилита, которая помогает скачивать Steam аккаунты по ссылкам с Яндекс.Диска, автоматически переименовывать файлы и извлекать информацию для входа.

### Быстрый старт

1. **Скачайте программу** из раздела [Releases](https://github.com/qnsi337/SteamYaDiskDownloader/releases)
2. **Распакуйте архив** в любую папку
3. **Создайте файл `links.txt`** и вставьте туда ваши ссылки на Яндекс.Диск (по одной на строку)
4. **Запустите `SteamYaDiskDownloader.exe`**
5. **Следуйте инструкциям** на экране

### Что делает этот инструмент?

Программа позволяет:
1. Автоматически скачать несколько Steam-аккаунтов с Яндекс.Диска по списку ссылок
2. Переименовать файлы в удобный формат (`логин.mafile`)
3. Создать текстовый файл с данными (`data.txt`) в удобном формате

### Подробная инструкция

#### Шаг 1: Подготовка
1. Скачайте `SteamYaDiskDownloader.exe` из раздела [Releases](https://github.com/qnsi337/SteamYaDiskDownloader/releases)
2. Распакуйте архив в любую папку

#### Шаг 2: Создание списка ссылок
1. Создайте текстовый файл `links.txt` в той же папке, где находится программа
2. Вставьте в файл ваши ссылки на Яндекс.Диск (по одной ссылке на строку)

#### Шаг 3: Скачивание файлов
1. Запустите программу `SteamYaDiskDownloader.exe`
2. При запросе пути к файлу просто нажмите Enter (программа автоматически использует файл `links.txt`)
3. При запросе папки для сохранения просто нажмите Enter для использования папки `accs` по умолчанию
4. Дождитесь завершения скачивания файлов

#### Шаг 4: Обработка файлов
1. После скачивания нажмите Enter, чтобы преобразовать файлы и создать `data.txt`
2. Программа переименует файлы из формата `логин+пароль+почта+пароль_от_почты.mafile` в `логин.mafile`
3. Также будет создан файл `data.txt` со всеми учетными данными

### Что содержится в файле data.txt?

После преобразования в файле `data.txt` будут строки в формате:
```
логин:пароль:почта:пароль_от_почты
```

Например:
```
steamuser123:pass123:user123@mail.ru:mailpass123
```

Это удобно для быстрого копирования данных при входе через SDA.

### Пример содержимого файла links.txt

```
https://yadi.sk/d/435AGH5Ppd9pGw
https://disk.yandex.by/d/435AGH5Ppd9pGw
```

### Важная информация

- Все файлы сохраняются в папку `accs` (создается автоматически)
- Программа работает с ссылками на Яндекс.Диск (yadi.sk или disk.yandex.ru)
- Если файл с именем `логин.mafile` уже существует, он будет заменен новым файлом
- **Рекомендуется сменить данные и пароли от аккаунта после получения!**

### Системные требования

- Windows 7/8/10/11
- Интернет-соединение для скачивания файлов
- Не требует установки Python или других программ

### Часто задаваемые вопросы

**В: Безопасна ли эта программа?**
О: Да, программа просто скачивает файлы по ссылкам Яндекс.Диска и не отправляет никаких данных на другие серверы.

**В: Требуется ли установка программы?**
О: Нет, просто скачайте EXE-файл и запустите его.

**В: Как использовать файл mafile?**
О: Файл .mafile нужно импортировать в Steam Desktop Authenticator (SDA) или другую программу для работы с Steam-аккаунтами, например, TradeOn SDA.

**В: Могу ли я скачать только один аккаунт?**
О: Да, просто добавьте только одну ссылку в файл links.txt.

**В: Что делать, если программа не запускается?**
О: Убедитесь, что вы распаковали архив полностью и у вас есть права на выполнение программы. В случае проблем обратитесь к продавцу.