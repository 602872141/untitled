from hashlib import md5

import requests
from urllib.parse import urlencode

Headers={

}
def get_page(offset):
    Query={
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery',

    }
    url='https://www.toutiao.com/search_content/?'+urlencode(Query)
    response = requests.get(url)
    print(url)
    if response.status_code == 200:
        return response.json()


# def get_images(json):
#     data=json.get('data')
#     if data:
#
#         for item in data:
#             title=item.get('title')
#             image_list=item.get('image_list')
#             if image_list:
#                 for ii in image_list:
#                     yield {
#                         'title':title,
#                         'url':ii.get('url')
#                     }
def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            # print(image_list)
            for image in image_list:
                yield {
                    'image': image.get('url'),
                    'title': title
                }


def save_inage(item):
    title=item.get('title')
    url=item.get('url')
    for image in url:
        reqsone = requests.get(image)
        if reqsone.status_code == 200:
            file_path='{0}/{1}.{2}'.format(image.get('tirle'),md5(reqsone.content).hexdigest,'jpg')
            
if __name__ == '__main__':
    page = get_page(0)
    print(page)
    for item in get_images(page):
        print(item)