import requests


def fix(original):
    response = requests.get(
        'https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy',
        params=dict(q=original, color_blindness=0)
    )
    return response.json()['message']['result']['notag_html']


assert fix('안녕 하세요') == '안녕하세요'
