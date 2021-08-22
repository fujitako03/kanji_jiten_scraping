import csv
import os

from config import config_utils
from scraping import scraping_utils


class KanjiList:
    def __init__(self) -> None:
        self.jyoyo_kanji_list = None
        self.jinmei_kanji_list = None
        self.kanji_list = None
    
    def get_jyoyo_kanji_list(self):
        """常用漢字とそのURL一覧を取得

        Returns:
            list: 常用漢字とurlのタプルのリスト
        """
        # configファイルからURLを取得
        url_config = config_utils.read_url_confing()
        jyoyo_url = url_config.jyoyo
        
        # スクレイピングで取得
        soup = scraping_utils.get_soup_from_url(jyoyo_url)
        kanji_table = soup.select('table')[1]  # 2つめが漢字一覧表
        kanji_list = [(a.get_text(), a.get('href'), '常用')for a in kanji_table.select('a')]

        # インスタンス変数に追加
        self.jyoyo_kanji_list = kanji_list


    def get_jinmei_kanji_list(self):
        """常用漢字とそのURL一覧を取得

        Returns:
            list: 常用漢字とurlのタプルのリスト
        """
        # configファイルからURLを取得
        url_config = config_utils.read_url_confing()
        jinmei_url = url_config.jinmei
        
        # スクレイピングで取得
        soup = scraping_utils.get_soup_from_url(jinmei_url)
        kanji_table = soup.select_one('table.kanjiitiran')  # 2つめが漢字一覧表
        kanji_list = [(a.get_text(), a.get('href'), '人名用') for a in kanji_table.select('a')]

        # インスタンス変数に追加
        self.jinmei_kanji_list = kanji_list
    
    def join_kanji_list(self):
        """常用漢字リストと常用漢字リストを結合する
        """
        self.kanji_list = [self.jyoyo_kanji_list + self.jinmei_kanji_list]
    
    def output_kanji_list(self):
        """取得した漢字一覧をtsvファイルに出力する
        """
        with open(os.path.join('output', 'kanji_list.tsv'), 'w') as f:
            writer = csv.writer(f, delimiter='\t')
            writer.writerow(['kanji','url', 'type'])
            for row in self.kanji_list:
                writer.writerows(row)


if __name__=='__main__':
    kl = KanjiList()
    kl.get_jyoyo_kanji_list()
    kl.get_jinmei_kanji_list()
    kl.join_kanji_list()
    kl.output_kanji_list()

