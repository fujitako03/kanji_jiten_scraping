import time

import bs4
import requests


def get_html(url, sleep_sec=1):
    """urlからhtmlを取得する

    Raises:
        Exception: htmlの取得が失敗

    Returns:
        str: 取得したhtml テキスト
    """
    time.sleep(sleep_sec)  # サーバ負荷軽減のため
    try:
        print(url)
        res = requests.get(url)
        if res.status_code == 200:
            # 成功
            return res.text
        else:
            # 失敗
            res.raise_for_status()
    except:
        raise Exception("htmlの取得に失敗しました")


def parse_html(html, parser='html.parser', file_encoding='utf-8'):
    """htmlをパースしBeautifulSoupオブジェクトを返す

    Args:
        html (str): HTMLテキスト
        parser (str, optional): パーサー Defaults to 'res.parser'.
        file_encoding (str, optional): htmlファイルのエンコード. Defaults to 'utf-8'.

    Raises:
        ValueError: htmlのパースに失敗したとき

    Returns:
        : BeautifulSoup
    """
    try:
        soup = bs4.BeautifulSoup(html, parser, from_encoding=file_encoding)
        return soup
    except:
        raise ValueError("htmlのパースに失敗しました")


def get_soup_from_url(url, sleep_time=1, parser='html.parser', file_encoding='utf-8'):
    """urlから該当のページをBeautifulSoupオブジェクトにして返す

    Args:
        url (str): url

    Returns:
        BeautifulSoup: 該当ページをパースしたBeautifulSoupオブジェクト
    """
    try:
        html = get_html(url, sleep_time)
        soup = parse_html(html, parser, file_encoding)
        return soup
    except:
        raise

if __name__=='__main__':
    url = 'https://kanjitisiki.com/zyouyou/'
    soup = get_soup_from_url(url)
    print(soup)
