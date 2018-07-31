from bs4 import BeautifulSoup
import requests
URL = 'https://www.pexels.com/search/'


def run():
    search = input('Search for free photos(The search must be in English): ')
    url = '{}{}'.format(URL, search)
    headers = {'User-Agent': 'Mozilla/5.0 4'} # Esto simula que estas entrando desde un navegador por lo que leí.
    web = requests.get(url, headers=headers)
    soup = BeautifulSoup(web.content, 'html.parser')
    urls_images = soup.find_all('img', {'class': 'photo-item__img'})
    for links in urls_images:
        source_image = links.get('src')
        image_url = source_image.split('?')[0]
        print(image_url)
        image_name = image_url.split('/')[-1]
        print('Downloading image {}'.format(image_name))
        print('image url: {}'.format(image_url))
        with open('{}'.format(image_name), 'wb') as f:
            tmp_url_image = requests.get(image_url, headers={'User-Agent': 'Mozilla/5.0.4'})
            f.write(tmp_url_image.content)


if __name__ == '__main__':
    run()
