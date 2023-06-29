import requests


def new_folder(tokenYA):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    params = {'path': 'TEST'}
    headers = {'Authorization': tokenYA}
    response = requests.put(url, params=params, headers=headers)
    return response


def main():
    with open('task_2/info/tokenYA.txt', 'r') as file_object:
        tokenYA = file_object.read().strip()
    print('123')
    return new_folder(tokenYA)


if __name__ == '__main__':
    main()