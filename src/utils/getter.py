import requests
from bs4 import BeautifulSoup
import utils.models as models


def get_site_1(city: str, type_cv: str) -> list[models.price]:
    """Function to get the price of site

    :argument: city: city name
    :return: list of price object
    :rtype: list[price]"""

    cookies = {
        '_ym_uid': '1707809186363580253',
        '_ym_d': '1707809186',
        '_ga': 'GA1.1.740557822.1707809186',
        'supportOnlineTalkID': 'NxOtFHegRKF7rlphae1amVNABiFtPSMT',
        'symfony': 'ddskoficflemlgagadld0ncs2v',
        '_mobile_detect': 'computer',
        '_s_cc': '0|computer|foo7IeDaenae',
        '_ym_isad': '1',
        'cf_clearance': 'aA8oqpmCQXyX5_40MnVn2Itgvrn1uqnjT04DNHjgCfc-1708182084-1.0-AUgdJM/sPkf28mwrBvt07LFkwJFfEs0WRhCnWZxII7nFB2Op0kS8y4MgjPNTV7OIf9KhAW/7I1GtIhBYvBJOBsM=',
        'au': '0',
        '_ga_TQQ6TKSGDH': 'GS1.1.1708182083.4.1.1708182208.0.0.0',
    }

    headers = {
        'authority': 'novosibirsk.restate.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': f'https://{city}.restate.ru',
        'referer': f'https://{city}.restate.ru/graph/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "YaBrowser";v="24.1", "Yowser";v="2.5"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 YaBrowser/24.1.0.0 Safari/537.36',
    }

    data = {
        'form': '9',
        'op': '1',
        'region': '60486',
        'type': f'{type_cv}',
        'period': '4',
        'influence': '3',
        'money': 'r',
    }

    response = requests.post(
        f'https://{city}.restate.ru/graph/ceny-prodazhi-kvartir/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('tbody')[1]

    result = []

    for tr in table.find_all('tr'):
        td = tr.find_all('td')
        date = td[0].text
        new = td[1].text
        old = td[3].text

        result.append(models.price(date, new, old))

    return result
