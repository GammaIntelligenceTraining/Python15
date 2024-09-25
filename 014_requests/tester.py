# import requests
# from requests.exceptions import HTTPError
#
#
#
# # 200 - success
# # 300 - redirect
# # 400 - client error
# # 500 - server error
#
# # r = requests.get('https://imgs.xkcd.com/comics/python.png', timeout=20)
# # print(r.content)
# # try:
# #     response = requests.get('http://api.github.com/invalid', timeout=20)
# #     response.raise_for_status()
# # except HTTPError as err:
# #     print(f'HTTP error: {err}')
# # else:
# #     print('Success')
#
# from bs4 import BeautifulSoup as BS
#
# url = 'https://gammatest.net/ru/kurs_python_105.php'
# response = requests.get(url, timeout=20)
#
# soup = BS(response.content, 'html.parser')
# # match = soup.find_all('a')
# # for m in match:
# #     print(m.get_attribute_list('href'))
# # match = soup.find('td', string='16. Регулярные выражения')
# # row = soup.css.select('table tr')
# # for r in row:
# #     res = r.find_all('td')
# #     for x in res:
# #         print(x.text)
# #     print('*' * 20)
#
# # match = soup.find_all(lambda x: x.has_attr('href'))
# # print(match)
#
# response = requests.get('https://jsonplaceholder.typicode.com/posts', timeout=20)
# result = response.json()
# for post in result:
#     print(post['title'])
#     print(post['body'])
#     print('*' * 20)
#
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
r = requests.get('https://www.google.com/search?q=eur+to+yen&rlz=1C1BNSD_enEE978EE978&oq=eur+to+yen&gs_lcrp=EgZjaHJvbWUyDggAEEUYJxg5GIAEGIoFMgcIARAAGIAEMgcIAhAAGIAEMgcIAxAAGIAEMgcIBBAAGIAEMgcIBRAAGIAEMgcIBhAAGIAEMgcIBxAAGIAEMgcICBAAGIAEMgcICRAAGIAE0gEIMjE5MWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8', headers=headers, timeout=20)
soup = BeautifulSoup()
print(soup.find('span', class_='DFlfde SwHCTb'))