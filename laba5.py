import requests
from dateutil import parser
from termcolor import colored
import emoji
from tabulate import tabulate

def main():
    # 1. requests
    try:
        response = requests.get("https://httpbin.org/get")
        print("Requests: Статус коду:", response.status_code)
    except Exception as e:
        print("Requests помилка:", e)

    # 2. python-dateutil
    try:
        date = parser.parse("2025-12-09")
        print("Dateutil: Рік =", date.year)
    except Exception as e:
        print("Dateutil помилка:", e)

    # 3. termcolor
    try:
        print(colored("Текст червоним кольором", "red"))
    except Exception as e:
        print("Termcolor помилка:", e)

    # 4. emoji
    try:
        print(emoji.emojize("Привіт :smile:"))
    except Exception as e:
        print("Emoji помилка:", e)

    # 5. tabulate
    try:
        data = [["Анатолій", 21], ["Богдан", 25]]
        print(tabulate(data, headers=["Ім'я", "Вік"]))
    except Exception as e:
        print("Tabulate помилка:", e)

if __name__ == "__main__":
    main()
