import requests
import os
import time
from colorama import init, Fore

# Инициализация цветовой схемы ANSI
init()

def init():
    print(Fore.GREEN + "Добро пожаловать!")
    time.sleep(1)
    print(Fore.YELLOW + "Запуск программы...")
    time.sleep(2)

def find_social_media():
    username = input("Введите имя пользователя для поиска: ")
    social_media_platforms = {'vk': 'https://vk.com/', 'doxbin': 'https://doxbin.org/', 'telegram': 'https://t.me/',
                              'youtube': 'https://youtube.com/user/', 'biolink': 'https://biol.ink/'}

    for platform, url_base in social_media_platforms.items():
        url = url_base + username

        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f'Найден профиль {username} на {platform}: {url}')
            else:
                print(f'Профиль {username} не найден на {platform}')
        except requests.exceptions.RequestException as e:
            print(f'Произошла ошибка при запросе к {platform}: {e}')

init()
time.sleep(2)

# Очистка консоли
os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.LIGHTYELLOW_EX, "Creator Muishiro connect: Fbi.ru")

find_social_media()