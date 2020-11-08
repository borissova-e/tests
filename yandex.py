import requests


def create_folder(headers, params):
    response = requests.put('https://cloud-api.yandex.net/v1/disk/resources', headers=headers,
                            params=params)
    return response

def check_folder(headers, params):
    response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/public?type=dir', headers=headers,
                            params=params)
    return response.json()



if __name__ == '__main__':
    tocken = input('Введите токен: ')
    oauth_tocken = ('OAuth ' + tocken)
    header = {'Authorization': oauth_tocken}
    param = {"path": "/file"}
    print(create_folder(header, param))
    print(check_folder(header, param))
