import requests


def main():
    locations = ['Лондон', 'аэропорт Шереметьево', 'Череповец']
    params = {
        'nMTmq': '',
        'lang': 'ru'
    }
    for location in locations:
        url = f'https://wttr.in/{location}'
        response = requests.get(url, params=params)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()